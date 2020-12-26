'''
Unit tests for Advent of Code 2020, Day 14.
James Jolley, jim.jolley [at] gmail.com
'''

import unittest
import day14 as pkg

class TestDay14(unittest.TestCase):
    def test_parse_mask(self):
        s = 'mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X\n'
        self.assertTupleEqual(pkg.parse_mask(s), ('mask', (2**36)-1-2, 64))
    
    def test_parse_write(self):
        s = 'mem[7] = 101\n'
        self.assertTupleEqual(pkg.parse_write(s), ('mem', 7, 101))
    
    def test_sum_mem(self):
        self.assertEqual(pkg.sum_mem(pkg.run_program('test_input/day14_t1.txt')), 165)
    
    def test_run_program_v2(self):
        self.assertEqual(pkg.sum_mem(pkg.run_program_v2('test_input/day14_t2.txt')), 208)
        

if __name__ == '__main__':
    unittest.main()
