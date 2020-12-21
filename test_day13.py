'''
Unit tests for Advent of Code 2020, Day 13.
James Jolley, jim.jolley [at] gmail.com
'''

import unittest
import day13 as pkg
from operator import mul

class TestDay13(unittest.TestCase):
    def test_next_bus(self):
        next = pkg.next_bus(*pkg.load_bus_info('test_input/day13_t1.txt'))
        self.assertEqual(mul(*next), 295)


if __name__ == '__main__':
    unittest.main()
