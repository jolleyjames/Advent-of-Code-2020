'''
Advent of Code 2020, Day 13.
James Jolley, jim.jolley [at] gmail.com
'''

from operator import mul
from functools import reduce

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

def match_offsets_crt(busses):
    '''
    Return the first timestamp such that all busses leave by the offsets
    prescribed by the input. Assuming that all bus IDs are prime numbers, 
    this can be solved by using the Chinese Remainder Theorem with Euler's
    totient.
    '''
    offset_with_id = enumerate(busses)
    offset_with_id = [(-x, int(p)) for x,p in offset_with_id if p!='x']
    offset_with_id = [(a%p, p) for a,p in offset_with_id]
    N = reduce(mul,[p for a,p in offset_with_id], 1)
    total = 0
    for a,p in offset_with_id:
        b = N // p
        b_inv = (b**(p-2))%p
        total += (a * b * b_inv)
        total %= N
    return total

if __name__ == '__main__':
    timestamp, busses = load_bus_info('input/day13.txt')
    # part 1
    print(mul(*next_bus(timestamp, busses)))
    # part 2
    print(match_offsets_crt(busses))
