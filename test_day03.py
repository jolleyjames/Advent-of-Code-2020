'''
Unit tests for Advent of Code 2020, Day 3.
James Jolley, jim.jolley [at] gmail.com
'''

import unittest
import day03 as pkg

class TestDay03(unittest.TestCase):
    def test_load_forest(self):
        f = pkg.load_forest('test_input/day03_t2.txt')
        self.assertEqual(f.x_size, 4)
        self.assertEqual(f.y_size, 6)
        expected_trees = set([(1,0),(0,1),(2,1),(3,2),(0,4),(1,4),(2,4),(3,4),(2,5),(3,5)])
        self.assertSetEqual(f.trees, expected_trees)
    
    def test_trees_encountered(self):
        f = pkg.load_forest('test_input/day03_t1.txt')
        self.assertEqual(pkg.trees_encountered(f, 3, 1), 7)
    