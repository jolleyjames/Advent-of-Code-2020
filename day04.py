'''
Advent of Code 2020, Day 4.
James Jolley, jim.jolley [at] gmail.com
'''

from re import fullmatch

def load_passports(path):
    '''
    Load passport data from the specified path. Passport data implemented
    as a dict of str keys to str values. Returns list of dicts.
    '''
    passports = []
    passport = {}
    with open(path) as file:
        for line in file:
            line = line.strip()
            if line:
                for data in line.split(' '):
                    pair = data.split(':')
                    passport[pair[0]] = pair[1]
            else:
                passports.append(passport)
                passport = {}
    passports.append(passport)
    return passports

default_fields = ('byr','iyr','eyr','hgt','hcl','ecl','pid')
def is_valid(passport, fields=default_fields):
    '''
    Returns True if all required fields are in the passport, False otherwise
    '''
    return all(field in passport for field in fields)

def value_in_range(s, digits, min_, max_):
    '''
    Returns True is string s has exact number of digits and is within
    the range min_ and max_. False otherwise.
    '''
    pattern = f'\\d{{{digits}}}'
    if fullmatch(pattern, s):
        value = int(s)
        return value >= min_ and value <= max_
    else:
        return False

def is_extra_valid(passport):
    '''
    Returns True if all required fields are present AND valid.
    '''
    if not is_valid(passport):
        return False
    # if here, all required fields are present; evaluate fields
    if not value_in_range(passport['byr'], 4, 1920, 2002):
        return False
    if not value_in_range(passport['iyr'], 4, 2010, 2020):
        return False
    if not value_in_range(passport['eyr'], 4, 2020, 2030):
        return False
    if passport['hgt'][-2:] == 'cm':
        digits, min_, max_ = 3, 150, 193
    elif passport['hgt'][-2:] == 'in':
        digits, min_, max_ = 2, 59, 76
    else:
        return False
    if not value_in_range(passport['hgt'][:-2], digits, min_, max_):
        return False
    if not fullmatch('#[\\da-f]{6}', passport['hcl']):
        return False
    if passport['ecl'] not in ('amb','blu','brn','gry','grn','hzl','oth'):
        return False
    if not value_in_range(passport['pid'], 9, 0, 999999999):
        return False
    return True

def count_valid(path, validator=is_valid):
    '''
    Return the number of valid passports from the file at the path.
    '''
    passports = load_passports(path)
    return sum(1 for p in passports if validator(p))

if __name__ == '__main__':
    # part 1
    print(count_valid('input/day04.txt', is_valid))
    # part 2
    print(count_valid('input/day04.txt', is_extra_valid))
    
