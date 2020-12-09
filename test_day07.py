'''
Unit tests for Advent of Code 2020, Day 7.
James Jolley, jim.jolley [at] gmail.com
'''

import unittest
import day07 as pkg

class TestDay07(unittest.TestCase):
    def test_load_rules(self):
        expected_rules = {
            'light red' : ((1, 'bright white'), (2, 'muted yellow')),
            'dark orange' : ((3, 'bright white'), (4, 'muted yellow')),
            'bright white' : ((1, 'shiny gold'),),
            'muted yellow' : ((2, 'shiny gold'), (9, 'faded blue')),
            'shiny gold' : ((1, 'dark olive'), (2, 'vibrant plum')),
            'dark olive' : ((3, 'faded blue'), (4, 'dotted black')),
            'vibrant plum' : ((5, 'faded blue'), (6, 'dotted black')),
            'faded blue' : (),
            'dotted black' : (),
        }
        self.assertDictEqual(pkg.load_rules('test_input/day07_t1.txt'), expected_rules)
    
    def test_contained_by(self):
        expected = {
            'bright white' : set(['light red','dark orange']),
            'muted yellow' : set(['light red','dark orange']),
            'shiny gold' : set(['bright white','muted yellow']),
            'faded blue' : set(['muted yellow','dark olive','vibrant plum']),
            'dark olive' : set(['shiny gold']),
            'vibrant plum' : set(['shiny gold']),
            'dotted black' : set(['dark olive','vibrant plum']),
        }
        rules = pkg.load_rules('test_input/day07_t1.txt')
        self.assertDictEqual(pkg.contained_by(rules), expected)
    
    def test_all_contained_by(self):
        expected = set(['bright white','muted yellow','dark orange','light red'])
        rules = pkg.load_rules('test_input/day07_t1.txt')
        self.assertSetEqual(pkg.all_contained_by(rules, 'shiny gold'), expected)

if __name__ == '__main__':
    unittest.main()
