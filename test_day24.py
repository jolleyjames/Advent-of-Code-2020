'''
Unit tests for Advent of Code 2020, Day 24.
James Jolley, jim.jolley [at] gmail.com
'''

import unittest
import day24 as pkg

class TestDay24(unittest.TestCase):
    def test_count_black(self):
        self.assertEqual(pkg.count_black('test_input/day24_t1.txt'), 10)
        
if __name__ == '__main__':
    unittest.main()
