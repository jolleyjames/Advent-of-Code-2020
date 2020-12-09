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

def count_total_bags_inside(rules, bag, evaluated_bags=None):
    '''
    Given a dict of bag colors keyed to the bags they can contain, return
    the total number of bags contained by the specified bag color.
    '''
    if bag not in rules:
        raise ValueError('bag not found in rules')
    # Keep a running total of the total number of bags within a bag
    if evaluated_bags is None:
        evaluated_bags = {}
    evaluated_bags[bag] = [0, list(rules[bag])]
    while evaluated_bags[bag][1]:
        count, inner_bag = evaluated_bags[bag][1][-1] 
        if inner_bag not in evaluated_bags:
            count_total_bags_inside(rules, inner_bag, evaluated_bags) 

        evaluated_bags[bag][0] += (count * (1+evaluated_bags[inner_bag][0])) 
        evaluated_bags[bag][1].pop() 
        
    return evaluated_bags[bag][0]


if __name__ == '__main__':
    # part 1
    rules = load_rules('input/day07.txt')
    print(len(all_contained_by(rules, 'shiny gold')))
    # part 2
    print(count_total_bags_inside(rules, 'shiny gold'))
