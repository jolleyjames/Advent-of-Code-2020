'''
Advent of Code 2020, Day 16.
James Jolley, jim.jolley [at] gmail.com
'''

def load_ranges_nrby_tix(path):
    '''
    Load just the valid value ranges and the nearby tickets.
    '''
    with open(path) as file:
        # Rules are at top of file. Parse rules until blank line encountered.
        ranges = []
        line = file.readline().strip()
        while len(line) > 0:
            line = line.split(': ')[1]
            n0, line = line.split('-', 1)
            n1, line = line.split(' or ')
            n2, n3 = line.split('-')
            n = [int(x) for x in (n0, n1, n2, n3)]
            if n[0] >= n[1] or n[1] >= n[2] or n[2] >= n[3]:
                raise ValueError(f'bad ranges {n[0]}-{n[1]}, {n[2]}-{n[3]}')
            ranges.extend([tuple(n[:2]),tuple(n[2:])])
            line = file.readline().strip()
        # At first blank line. Skip my ticket and nearby tickets header.
        for i in range(4):
            file.readline()
        # Load the nearby tickets.
        nearby_tix = [[int(s) for s in line.split(',')] for line in file.readlines()]
    return ranges, nearby_tix

def is_valid_field(field, ranges):
    '''
    True if field is in any of the ranges, False otherwise.
    '''
    for range in ranges:
        if range[0] <= field <= range[1]:
            return True
    return False

def error_rate(ranges, tix):
    '''
    Sum of all invalid fields.
    '''
    return sum(sum(field for field in ticket if not is_valid_field(field, ranges)) for ticket in tix)

if __name__ == '__main__':
    # part 1
    print(error_rate(*load_ranges_nrby_tix('input/day16.txt')))

