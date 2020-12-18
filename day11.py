'''
Advent of Code 2020, Day 11.
James Jolley, jim.jolley [at] gmail.com
'''

def load_seats(path):
    '''
    Load seat layout from the specified path. Returns a dict keyed by
    tuples of (row,column), keyed to a boolean: True if occupied, False
    if open.
    '''
    seats = {}
    with open(path) as file:
        row = 0
        for line in file.readlines():
            for col in range(len(line)):
                if line[col] == 'L':
                    seats[(row,col)] = False
                elif line[col] == '#':
                    seats[(row,col)] = True
            row += 1
    return seats

def get_neighbors(loc):
    '''
    Return sequence of neighboring locations.
    '''
    return ((loc[0]+a,loc[1]+b) for a in range(-1,2) for b in range(-1,2) if (a,b) != (0,0))

def occ_neighbors(seats, loc):
    '''
    Return number of occupied neighboring seats.
    '''
    occ = [seats.get(ngh,False) for ngh in get_neighbors(loc)]
    return len([s for s in occ if s])

def cycle(seats):
    '''
    Process a cycle of filling and leaving seats. seats is a dict returned
    from load_seats. The function modifies seats in place. Return the number
    of seats changed.
    '''
    # keep a copy of the previous status of the seats
    changes = 0
    prev_seats = dict(seats)
    for loc in seats:
        occ = occ_neighbors(prev_seats, loc)
        if not prev_seats[loc] and occ == 0:
            seats[loc] = True
            changes += 1
        elif prev_seats[loc] and occ >= 4:
            seats[loc] = False
            changes += 1
    return changes

def stabilize(seats):
    '''
    Process seat cycles until there are no changes.
    '''
    while cycle(seats) != 0:
        pass

def count_all_occ(seats):
    '''
    Number of occupied seats.
    '''
    return len([v for v in seats.values() if v])

if __name__ == '__main__':
    # part 1
    seats = load_seats('input/day11.txt')
    stabilize(seats)
    print(count_all_occ(seats))
    