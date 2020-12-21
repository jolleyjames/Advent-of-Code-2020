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
    
    def test_match_offsets_crt(self):
        _, busses = pkg.load_bus_info('test_input/day13_t1.txt')
        self.assertEqual(pkg.match_offsets_crt(busses), 1068781)
        _, busses = pkg.load_bus_info('test_input/day13_t2.txt')
        self.assertEqual(pkg.match_offsets_crt(busses), 3417)
        _, busses = pkg.load_bus_info('test_input/day13_t3.txt')
        self.assertEqual(pkg.match_offsets_crt(busses), 754018)
        _, busses = pkg.load_bus_info('test_input/day13_t4.txt')
        self.assertEqual(pkg.match_offsets_crt(busses), 779210)
        _, busses = pkg.load_bus_info('test_input/day13_t5.txt')
        self.assertEqual(pkg.match_offsets_crt(busses), 1261476)
        _, busses = pkg.load_bus_info('test_input/day13_t6.txt')
        self.assertEqual(pkg.match_offsets_crt(busses), 1202161486)



if __name__ == '__main__':
    unittest.main()
