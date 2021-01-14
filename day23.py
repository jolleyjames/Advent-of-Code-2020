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

if __name__ == '__main__':
    # part 1
    cups = input_to_list('789465123')
    for _ in range(100):
        move_to_destination(cups)
    print(cups_after_1(cups))

    
