'''
Advent of Code 2020, Day 1.
James Jolley, jim.jolley [at] gmail.com
'''

from operator import mul
from functools import reduce

def load_expense_report(path):
    '''
    Given a path to a text file of numbers, returns a list of ints.
    '''
    with open(path) as file:
        expenses = [int(line) for line in file.readlines()]
    return expenses

def find_sum(expenses, sum):
    '''
    Given a list of expenses and a sum, find the two expenses values that add
    to sum. Raises ValueError if no combination found.
    '''
    expenses_set = set(expenses)
    for expense in expenses:
        complement = sum - expense
        if complement in expenses_set:
            return (expense, complement)
    raise ValueError('no combination of numbers')

def product_of_sum(path, sum):
    '''
    Return the product of the two numbers that add to the sum.
    '''
    expenses = load_expense_report(path)
    addends = find_sum(expenses, sum)
    return reduce(mul, addends)

if __name__ == '__main__':
    # part 1
    print(product_of_sum('input/day01.txt', 2020))
    
