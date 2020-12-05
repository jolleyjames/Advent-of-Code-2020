'''
Advent of Code 2020, Day 5.
James Jolley, jim.jolley [at] gmail.com
'''

#B->1, F->0; R->1, L->0
table = str.maketrans({'B':'1', 'R':'1', 'F':'0','L':'0'})

def seat_id(bpass):
    '''
    Generate the seat ID from the boarding pass. Note that the boarding pass
    can be transformed to a binary integer by transforming 'B' and 'R' to 1,
    and 'F' and 'L' to 0.
    '''
    return int(bpass.translate(table), 2)

def load_seat_ids(path):
    '''
    Load the seat id values from the file at the specified path into a list.
    '''
    with open(path) as file:
        ids = [seat_id(bp.strip()) for bp in file.readlines()]
    return ids

def find_max_seat_id(path):
    '''
    Find the maximum seat ID value given the boarding pass values in the 
    specified file.
    '''
    return max(load_seat_ids(path))

def find_missing_seat_id(path):
    '''
    Find the seat id not in the file that is +1 and -1 from seats in the file.
    '''
    ids = load_seat_ids(path)
    ids = sorted(ids)
    for x in range(1, len(ids)):
        if ids[x]-ids[x-1] == 2:
            return ids[x] - 1
    raise ValueError('seat not found')

if __name__ == '__main__':
    # part 1
    print(find_max_seat_id('input/day05.txt'))
    # part 2
    print(find_missing_seat_id('input/day05.txt'))
