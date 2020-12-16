'''
Advent of Code 2020, Day 10.
James Jolley, jim.jolley [at] gmail.com
'''

from operator import mul

def load_adapters(path):
    '''
    Returns the output joltages of adapters in the specified path.
    '''
    with open(path) as file:
        return [int(line.strip()) for line in file.readlines()]
    
def add_start_and_end(joltages):
    '''
    The starting adapter joltage is 0, and the ending device joltage is 3
    more than the largest joltage. Append these joltages to the start and
    end of the list of joltages.
    '''
    joltages.sort()
    joltages.insert(0,0)
    joltages.append(joltages[-1]+3)

def count_differences(joltages, delta):
    '''
    When placed in order, counts the number of differences in joltage between
    adjacent devices, where the difference is delta. Assumes joltages are sorted.
    '''
    return sum(1 for i in range(1,len(joltages)) if joltages[i]-joltages[i-1]==delta)

def count_combinations(joltages, max_delta=3):
    '''
    Counts the number of unique combinations of joltages that can be
    achieved, given the contraint that adjacent joltages must be within
    max_delta. Assumes joltages are sorted.
    '''
    # Algorithm:
    # pass_count[final joltage] = 1
    # for joltage in next-to-last thru first joltage:
    #    pass_count[joltage] = sum(pass_count[adjacent joltage])
    # total combinations = pass_count[first joltage]
    pass_count = {joltages[-1] : 1}
    for i in range(len(joltages)-2, -1, -1):
        adj_joltages = [j for j in joltages[i+1 : i+1+max_delta] if j <= joltages[i]+max_delta]
        pass_count[joltages[i]] = sum(pass_count[adj] for adj in adj_joltages)
    return pass_count[joltages[0]]

if __name__ == '__main__':
    joltages = load_adapters('input/day10.txt')
    add_start_and_end(joltages)
    # part 1
    print(mul(*map(count_differences, (joltages,joltages), (1,3))))
    # part 2
    print(count_combinations(joltages))
