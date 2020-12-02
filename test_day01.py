'''
Unit tests for Advent of Code 2020, Day 1.
James Jolley, jim.jolley [at] gmail.com
'''

import unittest
import day01 as pkg

class TestDay01(unittest.TestCase):
    def test_load_expense_report(self):
        rep = [1721, 979, 366, 299, 675, 1456]
        self.assertEqual(pkg.load_expense_report('test_input/day01_t1.txt'), rep)

    def test_find_sum(self):
        expenses = pkg.load_expense_report('test_input/day01_t1.txt')
        entries = pkg.find_sum(expenses, 2020)
        self.assertEqual(len(entries), 2)
        self.assertIn(1721, entries)
        self.assertIn(299, entries)

    def test_find_sum_exc(self):
        expenses = pkg.load_expense_report('test_input/day01_t1.txt')
        # there should be no combination that adds to 1
        with self.assertRaises(ValueError):
            pkg.find_sum(expenses, 1)
    
    def test_product_of_sum(self):
        self.assertEqual(pkg.product_of_sum('test_input/day01_t1.txt', 2020), 514579)

if __name__ == '__main__':
    unittest.main()
