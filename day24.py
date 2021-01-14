'''
Advent of Code 2020, Day 24.
James Jolley, jim.jolley [at] gmail.com
'''

def hex_tile_pos(s):
    '''
    Return the (x,y) position of a hexagonal tile from a reference.
    '''
    pos = [0,0]
    while len(s) > 0:
        if s[0] in 'ew':
            pos[0] += (2 if s[0] == 'e' else -2)
            s = s[1:]
        elif s[0] in 'ns':
            pos[1] += (1 if s[0] == 's' else -1)
            if s[1] in 'ew':
                pos[0] += (1 if s[1] == 'e' else -1)
            else:
                raise ValueError(f'invalid direction {s[:2]}')
            s = s[2:]
        else:
            raise ValueError(f'invalid direction {s[0]}')
    return tuple(pos)

def count_black(path):
    '''
    Return the number of black tiles after processing the directions
    in the file at the path. All tiles start white.
    '''
    with open(path) as file:
        dirs = file.readlines()
    black_tiles = set()
    for s in dirs:
        pos = hex_tile_pos(s.strip())
        if pos in black_tiles:
            black_tiles.remove(pos)
        else:
            black_tiles.add(pos)
    return len(black_tiles)

if __name__ == '__main__':
    # part 1
    print(count_black('input/day24.txt'))
