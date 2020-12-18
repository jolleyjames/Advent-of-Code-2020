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

def get_visible(loc, seats):
    '''
    Return sequence of locations visible from the specified location.
    '''
    vis = []
    rows = set([a[0] for a in seats])
    cols = set([a[1] for a in seats])
    rows, cols = (set([a[i] for a in seats]) for i in (0,1))
    min_row, max_row = min(rows), max(rows)
    min_col, max_col = min(cols), max(cols)
    # up
    r, c = loc
    r -= 1
    while r >= min_row:
        if (r,c) in seats:
            vis.append((r,c))
            break
        else:
            r -= 1
    # up-right
    r, c = loc
    r -= 1
    c += 1
    while r >= min_row and c <= max_col:
        if (r,c) in seats:
            vis.append((r,c))
            break
        else:
            r -= 1
            c += 1
    # right
    r, c = loc
    c += 1
    while c <= max_col:
        if (r,c) in seats:
            vis.append((r,c))
            break
        else:
            c += 1
    # down-right
    r, c = loc
    r += 1
    c += 1
    while r <= max_row and c <= max_col:
        if (r,c) in seats:
            vis.append((r,c))
            break
        else:
            r += 1
            c += 1
    # down
    r, c = loc
    r += 1
    while r <= max_row :
        if (r,c) in seats:
            vis.append((r,c))
            break
        else:
            r += 1
    # down-left
    r, c = loc
    r += 1
    c -= 1
    while r <= max_row and c >= min_col:
        if (r,c) in seats:
            vis.append((r,c))
            break
        else:
            r += 1
            c -= 1
    # left
    r, c = loc
    c -= 1
    while c >= min_col:
        if (r,c) in seats:
            vis.append((r,c))
            break
        else:
            c -= 1
    # up-left
    r, c = loc
    r -= 1
    c -= 1
    while r >= min_row and c >= min_col:
        if (r,c) in seats:
            vis.append((r,c))
            break
        else:
            r -= 1
            c -= 1
    return vis

def occ_neighbors(seats, loc):
    '''
    Return number of occupied neighboring seats.
    '''
    occ = [seats.get(ngh,False) for ngh in get_neighbors(loc)]
    return len([s for s in occ if s])

def occ_visible(seats, loc):
    '''
    Return number of occupied visible seats.
    '''
    vis = [seats.get(ngh,False) for ngh in get_visible(loc, seats)]
    return len([s for s in vis if s])

def cycle(seats, f=occ_neighbors, leave_seat=4):
    '''
    Process a cycle of filling and leaving seats. seats is a dict returned
    from load_seats. The function modifies seats in place. Return the number
    of seats changed.
    '''
    # keep a copy of the previous status of the seats
    changes = 0
    prev_seats = dict(seats)
    for loc in seats:
        occ = f(prev_seats, loc)
        if not prev_seats[loc] and occ == 0:
            seats[loc] = True
            changes += 1
        elif prev_seats[loc] and occ >= leave_seat:
            seats[loc] = False
            changes += 1
    return changes

def stabilize(seats, f=occ_neighbors, leave_seat=4, debug=False):
    '''
    Process seat cycles until there are no changes.
    '''
    changed = cycle(seats, f, leave_seat)
    while changed != 0:
        if debug:
            print(f'stabilize: cycle returned {changed}')
        changed = cycle(seats, f, leave_seat)

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
    # part 2
    seats = load_seats('input/day11.txt')
    stabilize(seats, occ_visible, 5, True)
    print(count_all_occ(seats))

    