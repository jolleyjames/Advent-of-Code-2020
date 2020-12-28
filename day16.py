'''
Advent of Code 2020, Day 16.
James Jolley, jim.jolley [at] gmail.com
'''

from itertools import chain
from operator import mul
import numpy as np
from numpy.core.defchararray import startswith

def load_tix(path):
    '''
    Load the valid value ranges, the nearby tickets, and my ticket.
    '''
    with open(path) as file:
        # Rules are at top of file. Parse rules until blank line encountered.
        ranges = []
        line = file.readline().strip()
        while len(line) > 0:
            name, line = line.split(': ')
            n0, line = line.split('-', 1)
            n1, line = line.split(' or ')
            n2, n3 = line.split('-')
            n = [int(x) for x in (n0, n1, n2, n3)]
            if n[0] >= n[1] or n[1] >= n[2] or n[2] >= n[3]:
                raise ValueError(f'bad ranges {n[0]}-{n[1]}, {n[2]}-{n[3]}')
            ranges.append((name, tuple(n[:2]), tuple(n[2:])))
            line = file.readline().strip()
        # At first blank line. Skip header and load my ticket.
        file.readline() # header
        my_ticket = [int(s) for s in file.readline().split(',')]
        # Skip next blank line and 'nearby tickets' header.
        for i in range(2):
            file.readline()
        # Load the nearby tickets.
        nearby_tix = [[int(s) for s in line.split(',')] for line in file.readlines()]
    return ranges, nearby_tix, my_ticket

def is_valid_field(field, ranges):
    '''
    True if field is in any of the ranges, False otherwise.
    '''
    for range in ranges:
        if range[0] <= field <= range[1]:
            return True
    return False

def error_rate(all_ranges, ticket):
    '''
    Sum of all invalid fields.
    '''
    return sum(field for field in ticket if not is_valid_field(field, all_ranges))

def field_validity(field, ranges):
    '''
    Return the supplied ranges for which the field is valid. Ranges are
    expressed as an int where each bit represents the validity of the field
    for the range at that index.
    '''
    return sum(2**i for i in range(len(ranges)) if is_valid_field(field, ranges[i][1:]))

def ticket_validity(ticket, ranges):
    '''
    Return validity of all fields in the ticket, using the field_validity
    function.
    '''
    return [field_validity(field, ranges) for field in ticket]

def solve_fields(tix, ranges):
    '''
    Returns a sequence of ranges that is valid for every ticket.
    '''
    validities = [np.array(ticket_validity(ticket, ranges)) for ticket in tix]
    validities = np.bitwise_and.reduce(validities)
    solved_fields = set()
    while len(solved_fields) < len(ranges):
        # Look for solved fields.
        # Solved fields will be where there is only one valid range for
        # all fields on all tickets. These values will be integer powers of 2.
        log2 = np.log2(validities)
        for i in range(len(log2)):
            if log2[i].is_integer() and i not in solved_fields:
                # field at index i is for the range at index log2[i].
                # Blank out this bit for all other fields.
                and_v = np.array([2**len(ranges)-1-int(2**log2[i])] * len(validities))
                and_v[i] = 2**len(ranges)-1
                validities = np.bitwise_and(validities, and_v)
                solved_fields.add(i)
    # validities are now the 2-powers of the valid range for each
    # field index. return the range names.
    return [ranges[int(f)][0] for f in np.log2(validities)]


if __name__ == '__main__':
    ranges, nearby_tix, my_ticket = load_tix('input/day16.txt')
    # part 1
    all_ranges = list(chain(*[r[1:] for r in ranges]))
    nearby_tix.sort(key=lambda t: error_rate(all_ranges, t))
    print(sum(error_rate(all_ranges, ticket) for ticket in nearby_tix))
    # part 2
    nearby_tix = [ticket for ticket in nearby_tix if error_rate(all_ranges, ticket) == 0]
    solved = solve_fields(nearby_tix+[my_ticket], ranges)
    departure_ranges = [i for i in range(len(ranges)) if ranges[i][0].startswith('departure')]
    departure_indexes = [i for i in range(len(solved)) if solved[i].startswith('departure')]
    departure_values = [my_ticket[i] for i in departure_indexes]
    print(np.prod(departure_values))
