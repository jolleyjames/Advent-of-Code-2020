'''
Advent of Code 2020, Day 18.
James Jolley, jim.jolley [at] gmail.com
'''

from operator import add, mul

class Node:
    '''
    A representation of a binary arithmetic operation. Contains the 
    operation method, the left-hand-side argument, and the right-hand-side
    argument. Arguments will either be Nodes themselves, or int values.
    '''
    def __init__(self, op=None, lhs=None, rhs=None):
        self.op = op
        self.lhs = lhs
        self.rhs = rhs
    
    @staticmethod
    def side_value(side):
        '''
        Get the value of a left-hand or right-hand side argument.
        '''
        if type(side) == Node:
            return side.evaluate()
        else:
            return side
    
    def evaluate(self):
        '''
        Evaluate the expression defined by this Node.
        '''
        lhs_value, rhs_value = (Node.side_value(side) for side in (self.lhs,self.rhs))
        return (self.op)(lhs_value, rhs_value)


def parse_expression(s, advanced=False):
    '''
    Parse the string expression into a Node for evaluation.
    '''
    cursor = 0
    lhs, head = None, None
    # Expression alternates between value and operation tokens.
    op_next = False
    while cursor < len(s):
        # Skip ahead of whitespace.
        if s[cursor].isspace():
            cursor += 1
            continue
        if not op_next: # value expected
            value, end = None, None
            if s[cursor].isdigit():
                # find end of this integer token
                end = cursor + 1
                while end < len(s) and s[end].isdigit():
                    end += 1
                value = int(s[cursor:end])
            elif s[cursor] == '(':
                # find end of this parenthetical token
                end = cursor + 1
                paren_count = 1
                while paren_count != 0:
                    if s[end] == '(':
                        paren_count += 1
                    elif s[end] == ')':
                        paren_count -= 1
                    end += 1
                value = parse_expression(s[cursor+1:end-1], advanced)
                # add 0 to ensure higher precedence for parenthetical
                value = Node(add, value, 0) 
            if head is None:
                lhs = value
            else:
                head.rhs = value
                # in advanced math, add has higher precedence than mul
                if advanced and head.op == add and type(head.lhs) == Node and head.lhs.op == mul:
                    # perform the addition at head Node before the multiplication at head.lhs
                    # Node, by moving the mul to head and add to head.rhs
                    head = Node(mul, head.lhs.lhs, Node(add, head.lhs.rhs, head.rhs))
            cursor = end

        else: # operator expected
            op = {'+':add, '*':mul}[s[cursor]]
            if head is None:
                head = Node(op, lhs)
            else:
                new_head = Node(op, head)
                head = new_head
            cursor += 1
        op_next = not op_next
    return head

if __name__ == '__main__':
    with open('input/day18.txt') as file:
        expressions = file.readlines()
    # part 1
    print(sum(parse_expression(expr).evaluate() for expr in expressions))
    # part 2
    print(sum(parse_expression(expr,True).evaluate() for expr in expressions))
