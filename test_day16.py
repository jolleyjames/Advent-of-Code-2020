'''
Unit tests for Advent of Code 2020, Day 16.
James Jolley, jim.jolley [at] gmail.com
'''

import unittest
import day16 as pkg

class TestDay16(unittest.TestCase):
    def test_load_ranges_nrby_tix(self):
        exp_rngs = [(1,3),(5,7),(6,11),(33,44),(13,40),(45,50)]
        exp_tix = [[7,3,47],[40,4,50],[55,2,20],[38,6,12]]
        rngs, tix = pkg.load_ranges_nrby_tix('test_input/day16_t1.txt')
        self.assertSequenceEqual(rngs, exp_rngs)
        self.assertSequenceEqual(tix, exp_tix)
    
    def test_is_valid_field(self):
        rngs, _ = pkg.load_ranges_nrby_tix('test_input/day16_t1.txt')
        self.assertTrue(pkg.is_valid_field(40, rngs))
        self.assertFalse(pkg.is_valid_field(4, rngs))
    
    def test_error_rate(self):
        self.assertEqual(pkg.error_rate(*pkg.load_ranges_nrby_tix('test_input/day16_t1.txt')), 71)

        



if __name__ == '__main__':
    unittest.main()
