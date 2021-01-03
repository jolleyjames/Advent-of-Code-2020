'''
Advent of Code 2020, Day 19.
James Jolley, jim.jolley [at] gmail.com
'''

from itertools import product

def load_rules_and_messages(path):
    '''
    Load rules and messages from the specified path. Rules are keyed by
    integers to sequences. Messages are a sequence of strings.
    '''
    rules = {}
    with open(path) as file:
        # load rules
        line = file.readline().strip()
        while len(line) > 0:
            num, rule = line.split(': ')
            num = int(num)
            rule = rule.split()
            new_rule, this_rule = [], []
            for i in range(len(rule)):
                if rule[i].isdigit():
                    this_rule.append(int(rule[i]))
                elif rule[i] == '|':
                    new_rule.append(this_rule)
                    this_rule = []
                else:
                    new_rule = [rule[i].replace('"', '')]
            if len(this_rule) > 0:
                new_rule.append(this_rule)
            rules[num] = new_rule
            line = file.readline().strip()
        # load messages
        messages = [line.strip() for line in file.readlines()]
    return rules, messages

def reduce_rules(rules):
    '''
    Replace integer rules with strings.
    '''
    # track rules that directly map to all strings.
    all_str = set(k for k,v in rules.items() if all(type(e)==str for e in v))
    while len(all_str) < len(rules):
        for num in rules.keys() - all_str:
            i = 0
            while i < len(rules[num]):
                if type(rules[num][i]) != str:
                    if any(e in all_str for e in rules[num][i]):
                        extend_rules = product(*[rules[z] if z in all_str else [z] for z in rules[num][i]])
                        extend_rules = [list(rule) for rule in extend_rules]
                        del rules[num][i]
                        rules[num].extend(extend_rules)
                    else:
                        i += 1
                else:
                    i += 1
            # replace list of all strings with string
            for i in range(len(rules[num])):
                if all(type(e) == str for e in rules[num][i]):
                    rules[num][i] = ''.join(rules[num][i])
            # add num to all_str if all rules are strings
            if all(type(e)==str for e in rules[num]):
                all_str.add(num)

def matching_messages(messages, rules):
    '''
    Return the number of messages matching the rules.
    '''
    return len([m for m in messages if m in rules])

if __name__ == '__main__':
    # part 1
    r, m = load_rules_and_messages('input/day19.txt')
    reduce_rules(r)
    print(matching_messages(m, r[0]))
