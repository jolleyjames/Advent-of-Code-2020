'''
Unit tests for Advent of Code 2020, Day 25.
James Jolley, jim.jolley [at] gmail.com
'''

import unittest
from operator import mul
import day25 as pkg

class TestDay25(unittest.TestCase):
    def test_find_dh_privkey(self):
        self.assertEqual(pkg.find_dh_privkey((5764801,17807724)), 14897079)
        self.assertEqual(pkg.find_dh_privkey((17807724,5764801)), 14897079)

if __name__ == '__main__':
    unittest.main()
