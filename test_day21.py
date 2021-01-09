'''
Unit tests for Advent of Code 2020, Day 21.
James Jolley, jim.jolley [at] gmail.com
'''

import unittest
import day21 as pkg

class TestDay21(unittest.TestCase):
    def test_parse_food(self):
        s = 'mxmxvkd kfcds sqjhc nhms (contains dairy, fish)'
        exp = [['mxmxvkd','kfcds','sqjhc','nhms'],['dairy','fish']]
        self.assertEqual(pkg.parse_food(s), exp)
    
    def test_count_items(self):
        foods = pkg.load_foods('test_input/day21_t1.txt')
        exp = {
            'mxmxvkd': 3,
            'kfcds': 1,
            'sqjhc': 3,
            'nhms': 1,
            'trh': 1,
            'fvjkl': 2,
            'sbzzf': 2
        }
        self.assertDictEqual(pkg.count_items(foods), exp)
    
    def test_ingredient_to_allergen(self):
        foods = pkg.load_foods('test_input/day21_t1.txt')
        exp = [('mxmxvkd','dairy'), ('sqjhc','fish'), ('fvjkl','soy')]
        self.assertCountEqual(pkg.ingredient_to_allergen(foods), exp)
    
    def test_sum_ingr_without_allergen(self):
        foods = pkg.load_foods('test_input/day21_t1.txt')
        self.assertEqual(pkg.sum_ingr_without_allergen(foods), 5)
    
    def test_dangerous_ingr_list(self):
        foods = pkg.load_foods('test_input/day21_t1.txt')
        self.assertEqual(pkg.dangerous_ingr_list(foods), 'mxmxvkd,sqjhc,fvjkl')


        
if __name__ == '__main__':
    unittest.main()
