'''
Unit tests for Advent of Code 2020, Day 15.
James Jolley, jim.jolley [at] gmail.com
'''

import unittest
import day15 as pkg

class TestDay15(unittest.TestCase):
    def test_load_starting_numbers(self):
        expected = (6, 2, {0:0, 3:1})
        self.assertEqual(pkg.load_starting_numbers('test_input/day15_t1.txt'), expected)
    
    def test_offset_state(self):
        expected = ((0,-2), (3,-1))
        self.assertTupleEqual(pkg.offset_state(*pkg.load_starting_numbers('test_input/day15_t1.txt')[1:]), expected)
    
    def test_find_number(self):
        self.assertEqual(pkg.find_number('test_input/day15_t1.txt', 9), 0)
        self.assertEqual(pkg.find_number('test_input/day15_t1.txt', 2019), 436)
        self.assertEqual(pkg.find_number('test_input/day15_t2.txt', 2019), 1)
        self.assertEqual(pkg.find_number('test_input/day15_t3.txt', 2019), 10)
        self.assertEqual(pkg.find_number('test_input/day15_t4.txt', 2019), 27)
        self.assertEqual(pkg.find_number('test_input/day15_t5.txt', 2019), 78)
        self.assertEqual(pkg.find_number('test_input/day15_t6.txt', 2019), 438)
        self.assertEqual(pkg.find_number('test_input/day15_t7.txt', 2019), 1836)
        
        



if __name__ == '__main__':
    unittest.main()
