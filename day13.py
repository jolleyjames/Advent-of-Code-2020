'''
Advent of Code 2020, Day 13.
James Jolley, jim.jolley [at] gmail.com
'''

from operator import mul

def load_bus_info(path):
    '''
    Load the departure timestamp and the bus IDs from the specified path.
    '''
    with open(path) as file:
        timestamp = int(file.readline())
        ids = file.readline().strip().split(',')
    return timestamp, ids

def next_bus(timestamp, busses):
    '''
    Return a tuple containing the number of minutes to wait until the next
    bus leaves, with the id of the bus.
    '''
    busses = [int(id) for id in busses if id != 'x']
    return min([(-timestamp%id, id) for id in busses])

if __name__ == '__main__':
    timestamp, busses = load_bus_info('input/day13.txt')
    # part 1
    print(mul(*next_bus(timestamp, busses)))
