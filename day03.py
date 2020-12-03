'''
Advent of Code 2020, Day 3.
James Jolley, jim.jolley [at] gmail.com
'''

class Forest:
    '''
    Defines size of a forest with positions of trees.
    '''
    def __init__(self, x_size, y_size, trees):
        '''
        Initialize the forest. x_size and y_size are positive integers,
        trees is a set of 2-tuples of ints.
        '''
        self._x_size = x_size
        self._y_size = y_size
        self._trees = trees

    @property
    def x_size(self):
        return self._x_size
    
    @property
    def y_size(self):
        return self._y_size
    
    @property
    def trees(self):
        return self._trees
    
def load_forest(path):
    '''
    Load a Forest object from a text file.
    '''
    x_size, y_size, trees = 0, 0, set()
    with open(path) as file:
        for line in file:
            line = line.strip()
            x_size = len(line)
            for x in range(x_size):
                if line[x] == '#':
                    trees.add((x,y_size))
            y_size += 1
    return Forest(x_size, y_size, trees)

def trees_encountered(forest, x_move, y_move, start=(0,0)):
    '''
    Traverse the forest; return number of trees encountered.
    '''
    count = 0
    pos = start
    # continue until exit through bottom of forest
    while pos[1] < forest.y_size:
        if pos in forest.trees:
            count += 1
        pos = ((pos[0]+x_move)%forest.x_size, pos[1]+y_move)
    return count

if __name__ == '__main__':
    # part 1
    forest = load_forest('input/day03.txt')
    print(trees_encountered(forest, 3, 1))
    
        
