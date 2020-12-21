'''
Advent of Code 2020, Day 12.
James Jolley, jim.jolley [at] gmail.com
'''

import numpy as np

class Ship:
    '''
    Represents the position and direction of the ship.
    '''
    def __init__(self):
        self._pos = [0,0]
        self._dxn = 90 #east
    
    @property
    def pos(self):
        '''
        A 2-tuple representing the ship's position. [0] is north (negative)
        / south (positive); [1] is west (negative) / east (positive).
        '''
        return tuple(self._pos)
    
    @property
    def dxn(self):
        '''
        Direction the ship is facing. 0 == north, 90 == east, 180 == south,
        270 == east.
        '''
        return self._dxn
    
    def move(self, action):
        '''
        Move according to the action string.
        '''
        s, n = action[0], int(action[1:])
        if s == 'F':
            s = {0: 'N', 90: 'E', 180: 'S', 270: 'W'}[self.dxn]
        if s == 'N':
            self._pos[0] -= n
        elif s == 'S':
            self._pos[0] += n
        elif s == 'W':
            self._pos[1] -= n
        elif s == 'E':
            self._pos[1] += n
        elif s == 'L':
            self._dxn = (self._dxn - n)%360
        elif s == 'R':
            self._dxn = (self._dxn + n)%360
        else:
            raise ValueError(f'illegal action {s}')

def man_dist_after_actions(actions, ship_type=Ship):
    '''
    Return the Manhattan Distance of a ship starting at [0,0] after it
    takes each action.
    '''
    ship = ship_type()
    for action in actions:
        ship.move(action)
    return sum(map(abs, ship.pos))

class ShipWithWaypoint:
    '''
    Represents the positions of the ship and its waypoint
    '''
    def __init__(self):
        self._pos = np.array([0,0])
        self._waypoint = np.array([-1, 10])
    
    @property
    def pos(self):
        return tuple(self._pos)
    
    @property
    def waypoint(self):
        return tuple(self._waypoint)
    
    def move(self, action):
        '''
        Move the ship or waypoint according to the action string.
        '''
        s, n = action[0], int(action[1:])
        if s == 'F':
            self._pos += (self._waypoint * n)
        elif s == 'N':
            self._waypoint += np.array([-n, 0])
        elif s == 'S':
            self._waypoint += np.array([n, 0])
        elif s == 'W':
            self._waypoint += np.array([0, -n])
        elif s == 'E':
            self._waypoint += np.array([0, n])
        elif s in ('L', 'R'):
            if s == 'R':
                n = (360 - n)%360
            m = {0: np.array([[1,0],[0,1]]),
                 90: np.array([[0,-1],[1,0]]),
                 180: np.array([[-1,0],[0,-1]]),
                 270: np.array([[0,1],[-1,0]])}[n]
            self._waypoint = m @ self._waypoint
        else:
            raise ValueError(f'illegal action {s}')


if __name__ == '__main__':
    # part 1
    with open('input/day12.txt') as file:
        actions = file.readlines()
    print(man_dist_after_actions(actions))
    # part 2
    print(man_dist_after_actions(actions, ShipWithWaypoint))
