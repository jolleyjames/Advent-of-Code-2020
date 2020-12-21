'''
Unit tests for Advent of Code 2020, Day 12.
James Jolley, jim.jolley [at] gmail.com
'''

import unittest
import day12 as pkg

class TestDay12(unittest.TestCase):
    def test_man_dist_after_actions(self):
        with open('test_input/day12_t1.txt') as file:
            self.assertEqual(pkg.man_dist_after_actions(file.readlines()), 25)
    
    def test_waypoint(self):
        with open('test_input/day12_t1.txt') as file:
            self.assertEqual(pkg.man_dist_after_actions(file.readlines(),pkg.ShipWithWaypoint), 286)


if __name__ == '__main__':
    unittest.main()
