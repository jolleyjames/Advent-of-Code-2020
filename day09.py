'''
Advent of Code 2020, Day 9.
James Jolley, jim.jolley [at] gmail.com
'''

from collections import deque

class XmasSequence:
    '''
    Tracks the latest numbers in the XMAS sequence, and validates new
    numbers.
    '''
    def __init__(self, numbers):
        '''
        Initialize the sequence with the sequence of numbers. Assumes the
        sequence of numbers is the size of the preamble.
        '''
        self._preamble_len = len(numbers)
        # Set the valid sums. For easier ejection, store the sums as 3-tuples
        # where the first two values are the indexes used to create the sum,
        # the third value.
        self._sums = [(i,j,numbers[i]+numbers[j]) \
                      for i in range(len(numbers)) \
                      for j in range(i+1,len(numbers))]
        # Set the last numbers seen in the sequence.
        self._prev = deque(numbers)
        # Set the index of the next number to be added.
        self._next_index = self._preamble_len

    @property
    def preamble_len(self):
        return self._preamble_len
    
    @property
    def sums(self):
        return tuple(self._sums)
    
    @property
    def prev(self):
        return tuple(self._prev)

    @property
    def next_index(self):
        return self._next_index
    
    def is_valid(self, next):
        '''
        True if the next number is a valid sum of two of the previous
        numbers; False otherwise.
        '''
        return next in set([t[2] for t in self.sums])
    
    def add_next(self, next):
        '''
        Add the next number to the XMAS sequence, ejecting the oldest
        number and its sums.
        '''
        if not self.is_valid(next):
            raise ValueError('invalid sum')
        # Eject the oldest number and add the newest number.
        self._prev.popleft()
        self._prev.append(next)
        # Eject the oldest sums.
        self._sums.sort()
        self._sums = self._sums[self.preamble_len-1:]
        # Append the newest sums.
        self._sums += [(self.next_index-i,self.next_index,self._prev[-i-1]+next) for i in range(1,self.preamble_len)]
        # Update the next index.
        self._next_index += 1

def load_numbers(path):
    with open(path) as file:
        return [int(line.strip()) for line in file.readlines()]

def first_invalid(numbers, preamble_len=25):
    '''
    Returns the first invalid XMAS sequence number in the sequence
    of numbers.
    '''
    preamble = numbers[:preamble_len]
    xs = XmasSequence(preamble)
    for i in range(preamble_len, len(numbers)):
        next = numbers[i]
        try:
            xs.add_next(next)
        except ValueError:
            return next
    raise ValueError('no invalid number found')

def find_contiguous_sum(numbers, preamble_len=25):
    '''
    Returns a tuple of the range of indexes (starting inclusive, ending
    exclusive) that sum to the first invalid number in the sequence of
    numbers.
    '''
    #TODO implement me
    pass

if __name__ == '__main__':
    # part 1
    print(first_invalid(load_numbers('input/day09.txt')))
