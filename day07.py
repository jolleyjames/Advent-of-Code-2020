'''
Advent of Code 2020, Day 7.
James Jolley, jim.jolley [at] gmail.com
'''

def parse_rule(rule):
    '''
    Parses a string containing a bag rule. Returns a tuple: element [0] is the
    color of the bag; elements [1] and later are 2-tuples containing the number
    and color of each bag type that must be contained.
    '''
    if ' bags contain ' not in rule:
        raise ValueError('bad rule syntax (1)')
    color, contained = rule.split(' bags contain ')
    contained = contained.rstrip('.')
    if contained == 'no other bags':
        contained = []
    else:
        contained = contained.split(', ')
        contained = [bag.split(' ')[:-1] for bag in contained]
        contained = [(int(bag[0]), f'{bag[1]} {bag[2]}') for bag in contained]
    return (color,) + tuple(contained)


def load_rules(path):
    '''
    Load the bag rules from the specified path. Returns a dict keyed by a
    string containing the color of the bag.
    '''
    rules_dict = {}
    with open(path) as file:
        for line in file:
            line = line.strip()
            rule = parse_rule(line)
            rules_dict[rule[0]] = rule[1:]
    return rules_dict

def contained_by(rules):
    '''
    Given a dict of bag colors keyed to the bags they can contain, return
    a dict of bag colors keyed to the bags in which they can *directly*
    contained.
    '''
    contained_dict = {}
    for k,v in rules.items():
        for bag in v:
            if bag[1] in contained_dict:
                contained_dict[bag[1]].add(k)
            else:
                contained_dict[bag[1]] = set((k,))
    return contained_dict

def all_contained_by(rules, bag):
    '''
    Given a dict of bag colors keyed to the bags they contain, and a 
    bag color, find all bags which may directly or indirectly contain
    a bag of the specified color.
    '''
    contained = contained_by(rules)
    # all bags which may contain the specified bag
    all_containing = set()
    # bags to evaluate
    eval_queue = [bag]
    while eval_queue:
        this = eval_queue.pop()
        if this in contained:
            for containing in contained[this]:
                if containing not in all_containing:
                    all_containing.add(containing)
                    eval_queue.append(containing)
    return all_containing

if __name__ == '__main__':
    # part 1
    rules = load_rules('input/day07.txt')
    print(len(all_contained_by(rules, 'shiny gold')))