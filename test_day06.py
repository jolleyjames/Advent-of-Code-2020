'''
Unit tests for Advent of Code 2020, Day 6.
James Jolley, jim.jolley [at] gmail.com
'''

import unittest
import day06 as pkg

class TestDay06(unittest.TestCase):
    def test_load_declarations(self):
        groups = pkg.load_declarations('test_input/day06_t1.txt')
        self.assertEqual(len(groups), 5)
        for x in range(3):
            self.assertSetEqual(groups[x], set('abc'))
        self.assertSetEqual(groups[3], set('a'))
        self.assertSetEqual(groups[4], set('b'))
    
    def test_count_yeses(self):
        groups = pkg.load_declarations('test_input/day06_t1.txt')
        self.assertEqual(pkg.count_yeses(groups), 11)

    def test_load_declarations_2(self):
        groups = pkg.load_declarations_2('test_input/day06_t1.txt')        
        self.assertEqual(len(groups), 5)
        self.assertSetEqual(groups[0], set('abc'))
        self.assertSetEqual(groups[1], set())
        self.assertSetEqual(groups[2], set('a'))
        self.assertSetEqual(groups[3], set('a'))
        self.assertSetEqual(groups[4], set('b'))
    

if __name__ == '__main__':
    unittest.main()
