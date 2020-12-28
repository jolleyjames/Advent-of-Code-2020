'''
Advent of Code 2020, Day 15.
James Jolley, jim.jolley [at] gmail.com
'''

from datetime import datetime

def load_starting_numbers(path):
    '''
    Load the starting numbers from the specified path. Returns a tuple
    containing the last number in the starting numbers, the index to be
    used for this next number, and a dict of the other starting numbers
    keyed to the times they were seen.
    '''
    with open(path) as file:
        start = [int(n) for n in file.readline().split(',')]
    if len(set(start)) != len(start):
        raise ValueError('starting numbers must be unique')
    current_state = {}
    for i in range(len(start)-1):
        current_state[start[i]] = i
    return start[-1], len(start)-1, current_state

def offset_state(offset, current_state):
    '''
    Return a copy of the current state with last-seen values offset by the
    specified number. For example, if the current state says 0 was last seen
    at time 4, and the offset is 10, then the offset state will
    say that 0 was last seen at time -6.
    '''
    new_state = [(k, v-offset) for k,v in current_state.items()]
    new_state.sort()
    return tuple(new_state)

def find_number(path_sn, index):
    '''
    Return the number spoken after the turn specified by the index. Note,
    the function uses a 0-based index, so the 2020th number will be the 
    number spoken at index 2019.
    '''
    next_number, next_index, current_state = load_starting_numbers(path_sn)
    if next_index > index:
        raise ValueError('index must be at least the number of the starting numbers')
    while next_index < index:
        this_number, this_index = next_number, next_index
        next_number = this_index - current_state.get(this_number, this_index)
        current_state[this_number] = this_index
        next_index += 1
    return next_number

if __name__ == '__main__':
    # part 1
    print(find_number('input/day15.txt', 2019))
    # part 2
    print(find_number('input/day15.txt', 30000000-1))
    
