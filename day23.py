'''
Advent of Code 2020, Day 23.
James Jolley, jim.jolley [at] gmail.com
'''

def input_to_list(s):
    '''
    Take a string containing all digits and transform into a list containing
    ints.
    '''
    return [int(c) for c in s]

def move_to_destination(cups):
    '''
    Given a list of cups, find the destination and move cups at index slice
    [1:4] just past the destination. Current cup is always at index 0.
    '''
    pick_up = [cups.pop(1) for _ in range(3)]
    search_cups = [cup for cup in cups[1:] if cup < cups[0]]
    if len(search_cups) == 0:
        search_cups = cups[1:]
    dest_value = max(search_cups)
    dest_index = cups.index(dest_value)
    for i in range(len(pick_up)):
        cups.insert(dest_index+1+i, pick_up[i])
    # keep current cup at index 0
    cups.append(cups.pop(0))

def cups_after_1(cups):
    '''
    Return a string representation of all cups starting with the cup
    immediately after the cup with value 1.
    '''
    one_index = cups.index(1)
    return ''.join(str(c) for c in cups[one_index+1:] + cups[:one_index])

class Node:
    '''
    Represents a node within a circular linked list.
    '''
    def __init__(self, value, nxt=None):
        self._value = value
        self.nxt = nxt
    
    @property
    def value(self):
        return self._value
    
def input_to_huge_list(s, limit = 1000000):
    '''
    Take the input string and create a linked list of one million Nodes.
    Returns a dictionary of each Node keyed by their values.
    '''
    d = {}
    head = None
    first = None
    for c in s:
        new_node = Node(int(c))
        if first is None:
            first = new_node
        else:
            head.nxt = new_node
        head = new_node
        d[head.value] = head
    next_value = max(d.keys())+1
    for i in range(next_value, limit+1):
        new_node = Node(i)
        head.nxt = new_node
        head = new_node
        d[head.value] = head
    # connect the last Node to the first Node
    head.nxt = first
    return d

def move_to_destination_ll(current, dict_all_nodes):
    '''
    Given a reference to the current cup as a Node and a dict of all Nodes in
    the linked list, find the destination and move the three cups following 
    the current cup just past the destination.
    '''
    pick_up_values = []
    head = current
    for _ in range(3):
        head = head.nxt
        pick_up_values.append(head.value)
    dest = current.value - 1
    while dest <= 0 or dest in pick_up_values:
        if dest <= 0:
            dest = max(dict_all_nodes.keys())
        if dest in pick_up_values:
            dest -= 1
    dest = dict_all_nodes[dest]
    pick_up_head = current.nxt
    after_dest = dest.nxt
    current.nxt = current.nxt.nxt.nxt.nxt
    dest.nxt = pick_up_head
    dest.nxt.nxt.nxt.nxt = after_dest

def product_of_nodes(s):
    '''
    Given the starting cup values as a string, run ten million iterations using
    one million cups, and return the product of the cups to the right of the 
    cup with value 1.
    '''
    d = input_to_huge_list(s)
    current = d[int(s[0])]
    for _ in range(10000000):
        move_to_destination_ll(current, d)
        current = current.nxt
    one = d[1]
    return one.nxt.value * one.nxt.nxt.value

if __name__ == '__main__':
    # part 1
    cups = input_to_list('789465123')
    for _ in range(100):
        move_to_destination(cups)
    print(cups_after_1(cups))
    # part 2
    print(product_of_nodes('789465123'))
