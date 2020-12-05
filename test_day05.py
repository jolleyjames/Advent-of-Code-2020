'''
Unit tests for Advent of Code 2020, Day 5.
James Jolley, jim.jolley [at] gmail.com
'''

import unittest
import day05 as pkg

class TestDay05(unittest.TestCase):
    def test_seat_id(self):
        self.assertEqual(pkg.seat_id('BFFFBBFRRR'), 567)
        self.assertEqual(pkg.seat_id('FFFBBBFRRR'), 119)
        self.assertEqual(pkg.seat_id('BBFFBBFRLL'), 820)
    
    def test_find_max_seat_id(self):
        self.assertEqual(pkg.find_max_seat_id('test_input/day05_t1.txt'), 820)

if __name__ == '__main__':
    unittest.main()
