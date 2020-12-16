'''
Unit tests for Advent of Code 2020, Day 10.
James Jolley, jim.jolley [at] gmail.com
'''

import unittest
import day10 as pkg

class TestDay10(unittest.TestCase):
    def test_count_differences(self):
        a = [pkg.load_adapters(f'test_input/day10_t{n}.txt') for n in (1,2)]
        for i in range(len(a)):
            pkg.add_start_and_end(a[i])
        self.assertEqual(pkg.count_differences(a[0],1), 7)
        self.assertEqual(pkg.count_differences(a[0],3), 5)
        self.assertEqual(pkg.count_differences(a[1],1), 22)
        self.assertEqual(pkg.count_differences(a[1],3), 10)
    
    def test_count_combinations(self):
        a = [pkg.load_adapters(f'test_input/day10_t{n}.txt') for n in (1,2)]
        for i in range(len(a)):
            pkg.add_start_and_end(a[i])
        self.assertEqual(pkg.count_combinations(a[0]), 8)
        self.assertEqual(pkg.count_combinations(a[1]), 19208)

if __name__ == '__main__':
    unittest.main()
