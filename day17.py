'''
Advent of Code 2020, Day 17.
James Jolley, jim.jolley [at] gmail.com
'''

def load_cubes(path, z=0):
    '''
    Load the 2-d slice of cubes from the specified path. Returns a set
    containing coordinates of active cubes; coordinates are 3-tuples of
    the cube's x, y, and z coordinates.
    '''
    cubes = set()
    y = 0
    with open(path) as file:
        for line in file.readlines():
            x = 0
            for c in line.strip():
                if c == '#':
                    cubes.add((x,y,z))
                elif c == '.':
                    # missing coordinate indicates inactive cube
                    pass
                else:
                    raise ValueError(f'invalid char {c} @ row {y+1} col {x+1}')
                x += 1
            y += 1
    return cubes

def load_cubes_4d(path, w=0, z=0):
    return set((w, *c) for c in load_cubes(path, z))

def next_cube_state(is_active, active_nghbr_count):
    '''
    Determine if this cube will be active in the next step, based on its
    current active status and the number of its active neighbors.
    '''
    return (is_active and active_nghbr_count == 2) or active_nghbr_count == 3

def active_neighbors(cube, cubes, reflect_z0=True):
    '''
    Return the number of active cubes neighboring the specified cube.
    '''
    active_nghbr_coords = [(x,y,z) for x in range(cube[0]-1,cube[0]+2) \
                                   for y in range(cube[1]-1,cube[1]+2) \
                                   for z in range(cube[2]-1,cube[2]+2) \
                                   if (x,y,z) != cube and (x,y,z) in cubes]
    if reflect_z0 and cube[2] == 0:
        active_nghbr_coords.extend([(c[0],c[1],-c[2]) for c in active_nghbr_coords if c[2] == 1])
    return len(active_nghbr_coords)

def active_neighbors_4d(cube, cubes, reflect_wz0=True):
    '''
    An ideal solution would handle an unlimited number
    of dimensions. Candidate for refactoring.
    '''
    active_nghbr_coords = [(w,x,y,z) for w in range(cube[0]-1,cube[0]+2) \
                                     for x in range(cube[1]-1,cube[1]+2) \
                                     for y in range(cube[2]-1,cube[2]+2) \
                                     for z in range(cube[3]-1,cube[3]+2) \
                                     if (w,x,y,z) != cube and (w,x,y,z) in cubes]
    if reflect_wz0:
        if cube[0] == 0:
            active_nghbr_coords.extend([(-c[0],c[1],c[2],c[3]) for c in active_nghbr_coords if c[0] == 1])
        if cube[3] == 0:
            active_nghbr_coords.extend([(c[0],c[1],c[2],-c[3]) for c in active_nghbr_coords if c[3] == 1])
    return len(active_nghbr_coords)

def cycle(cubes, f=next_cube_state, reflect_z0=True):
    '''
    Run the set of cubes through a cycle using the specified function
    to determine the active status of each cube.
    '''
    xs, ys, zs = list(zip(*list(cubes)))
    xrng, yrng, zrng = [[t[0](v)+t[1] for t in ((min,-1),(max,2))] for v in (xs, ys, zs)]
    if reflect_z0 and zrng[0] != -1:
        raise ValueError('z values not reflected along 0 plane')
    elif reflect_z0:
        zrng[0] = 0
    new_cubes = set()
    for x in range(*xrng):
        for y in range(*yrng):
            for z in range(*zrng):
                cube = (x,y,z)
                if f(cube in cubes, active_neighbors(cube, cubes, reflect_z0)):
                    new_cubes.add(cube)
    return new_cubes

def cycle_4d(cubes, f=next_cube_state, reflect_wz0=True):
    '''
    An ideal solution would handle an unlimited number
    of dimensions. Candidate for refactoring.
    '''
    ws, xs, ys, zs = list(zip(*list(cubes)))
    wrng, xrng, yrng, zrng = [[t[0](v)+t[1] for t in ((min,-1),(max,2))] for v in (ws, xs, ys, zs)]
    if reflect_wz0 and wrng[0] != -1:
        raise ValueError('w values not reflected along 0 plane')
    if reflect_wz0 and zrng[0] != -1:
        raise ValueError('z values not reflected along 0 plane')
    elif reflect_wz0:
        wrng[0] = 0
        zrng[0] = 0
    new_cubes = set()
    for w in range(*wrng):
        for x in range(*xrng):
            for y in range(*yrng):
                for z in range(*zrng):
                    cube = (w,x,y,z)
                    if f(cube in cubes, active_neighbors_4d(cube, cubes, reflect_wz0)):
                        new_cubes.add(cube)
    return new_cubes

def count_active_cubes(cubes, reflect_z0=True):
    '''
    Count the number of active cubes.
    '''
    if reflect_z0:
        return 2*len(cubes)-len([c for c in cubes if c[2] == 0])
    else:
        return len(cubes)

def count_active_cubes_4d(cubes, reflect_wz0=True):
    '''
    An ideal solution would handle an unlimited number
    of dimensions. Candidate for refactoring.
    '''
    if reflect_wz0:
        def mag(cube):
            if (cube[0],cube[3]) == (0,0):
                return 1
            elif (cube[0] == 0 and cube[3] != 0) or (cube[0] != 0 and cube[3] == 0):
                return 2
            else:
                return 4
        return sum(mag(cube) for cube in cubes)
    else:
        return len(cubes)

if __name__ == '__main__':
    # part 1
    cubes = load_cubes('input/day17.txt')
    for _ in range(6):
        cubes = cycle(cubes)
    print(count_active_cubes(cubes)) 
    # part 2
    cubes = load_cubes_4d('input/day17.txt')
    for _ in range(6):
        cubes = cycle_4d(cubes)
    print(count_active_cubes_4d(cubes)) 
