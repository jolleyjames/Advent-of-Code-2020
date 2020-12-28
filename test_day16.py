'''
Unit tests for Advent of Code 2020, Day 16.
James Jolley, jim.jolley [at] gmail.com
'''

import unittest
from itertools import chain
import day16 as pkg

class TestDay16(unittest.TestCase):
    def test_load_tix(self):
        exp_rngs = [('class',(1,3),(5,7)),('row',(6,11),(33,44)),('seat',(13,40),(45,50))]
        exp_tix = [[7,3,47],[40,4,50],[55,2,20],[38,6,12]]
        exp_my_tick = [7,1,14]
        rngs, tix, my_tick = pkg.load_tix('test_input/day16_t1.txt')
        self.assertSequenceEqual(rngs, exp_rngs)
        self.assertSequenceEqual(tix, exp_tix)
        self.assertSequenceEqual(my_tick, exp_my_tick)
    
    def test_is_valid_field(self):
        rngs, _, __ = pkg.load_tix('test_input/day16_t1.txt')
        rngs = list(chain(*[r[1:] for r in rngs]))
        self.assertTrue(pkg.is_valid_field(40, rngs))
        self.assertFalse(pkg.is_valid_field(4, rngs))
    
    def test_error_rate(self):
        ranges, nearby_tix, _ = pkg.load_tix('test_input/day16_t1.txt')
        all_ranges = list(chain(*[r[1:] for r in ranges]))
        self.assertEqual(sum(pkg.error_rate(all_ranges, ticket) for ticket in nearby_tix), 71)
    
    def test_solve_fields(self):
        ranges, nearby_tix, my_ticket = pkg.load_tix('test_input/day16_t2.txt')
        solved = pkg.solve_fields(nearby_tix + [my_ticket], ranges)
        self.assertSequenceEqual(solved, ['row','class','seat'])
        
if __name__ == '__main__':
    unittest.main()
