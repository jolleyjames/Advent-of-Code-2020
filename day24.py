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

def load_black(path):
    '''
    Return the set of positions of black tiles after processing the directions
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
    return black_tiles

def neighbors(pos):
    '''
    Get the six neighbors of the hexagonal tile at the specified position.
    '''
    x,y = pos
    return [(x-2,y),(x+2,y),(x-1,y-1),(x+1,y-1),(x-1,y+1),(x+1,y+1)]

def cycle(black):
    '''
    Flip all black and white tiles according to the rules. The parameter
    set contains the complete set of black tiles' positions. All other
    positions contain white tiles.
    '''
    # Find all white tiles neighboring black tiles. Other white tiles
    # which don't neighbor black tiles are not important, as white tiles
    # with no adjacent black tiles will remain white.
    white = set()
    for b in black:
        white |= set(nbr for nbr in neighbors(b) if nbr not in black)
    # black tiles after this cycle are stored here
    new_black = set()
    # keep black tiles that will remain black
    for b in black:
        if len([nbr for nbr in neighbors(b) if nbr in black]) in (1,2):
            new_black.add(b)
    # add tiles that switch from white to black
    for w in white:
        if len([nbr for nbr in neighbors(w) if nbr in black]) == 2:
            new_black.add(w)
    return new_black



if __name__ == '__main__':
    black = load_black('input/day24.txt')
    # part 1
    print(len(black))
    # part 2
    for _ in range(100):
        black = cycle(black)
    print(len(black))
