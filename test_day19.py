'''
Unit tests for Advent of Code 2020, Day 19.
James Jolley, jim.jolley [at] gmail.com
'''

import unittest
import day19 as pkg

class TestDay19(unittest.TestCase):
    def test_matching_messages(self):
        r, m = pkg.load_rules_and_messages('test_input/day19_t1.txt')
        pkg.reduce_rules(r)
        self.assertEqual(pkg.matching_messages(m, r[0]), 2)

        
if __name__ == '__main__':
    unittest.main()
