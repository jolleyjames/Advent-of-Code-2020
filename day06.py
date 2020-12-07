'''
Advent of Code 2020, Day 6.
James Jolley, jim.jolley [at] gmail.com
'''

def load_declarations(path):
    '''
    Load customs declaration forms from the specified path. Returns a list
    of sets, where each set contains the questions answered "yes" by
    someone in the group.
    '''
    groups, form = [], set()
    with open(path) as file:
        for line in file:
            line = line.strip()
            if line:
                form |= set(line)
            else:
                groups.append(form)
                form = set()
    groups.append(form)
    return groups

def load_declarations_2(path):
    '''
    Load declarations according to updated rules in Part 2 -- every set
    will contain questions answered "yes" by *everyone* in the group.
    '''
    groups, form = [], None
    with open(path) as file:
        for line in file:
            line = line.strip()
            if line:
                if form is None:
                    form = set(line)
                else:
                    form &= set(line)
            else:
                groups.append(form)
                form = None
    groups.append(form)
    return groups


def count_yeses(groups):
    '''
    Return the sum of questions answered yes for all groups. Expects an
    iterable of sets containing the questions answered "yes" for each
    group.
    '''
    return sum(len(group) for group in groups)

if __name__ == '__main__':
    # part 1
    groups = load_declarations('input/day06.txt')
    print(count_yeses(groups))
    # part 2
    groups = load_declarations_2('input/day06.txt')
    print(count_yeses(groups))
