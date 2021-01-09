'''
Advent of Code 2020, Day 21.
James Jolley, jim.jolley [at] gmail.com
'''

from itertools import chain, groupby

def parse_food(s):
    '''
    Parse a string defining a food into a 2-d list containing ingredients
    and allergens, as strings.
    '''
    ingredients, allergens = s.split(' (contains ')
    # remove final ')' from allergens
    allergens = allergens[:-1]
    return [ingredients.split(), allergens.split(', ')]

def load_foods(path):
    '''
    Load foods from path. Each food is a 2-d list containing ingredients and
    allergens, as strings.
    '''
    with open(path) as file:
        return [parse_food(line.strip()) for line in file.readlines()]

def count_items(foods, index=0):
    '''
    Return a dict containing each items and the number of times
    each items in the sequence of foods.
    '''
    all_items = list(chain(*[food[index] for food in foods]))
    all_items.sort()
    return {k:len(list(g)) for k,g in groupby(all_items)}

def ingredient_to_allergen(foods):
    '''
    Find which ingredients contain which allergens, using the list
    of foods. Returns sequence of 2-tuples containing ingredient and
    allergen.
    '''
    # Make a copy of foods
    foods = [[list(l) for l in food] for food in foods]
    # Get a list of all allergens
    allergens = list(count_items(foods, 1).keys())
    # The allergen-ingredient combos found
    found = {}
    while len(found) < len(allergens):
        is_found = False
        # Find an ingredient that maps to an allergen.
        for i in range(len(allergens)):
            allergen = allergens[i]
            if allergen in found:
                continue
            # Find all ingredients that could contain this allergen
            ingr_set = None
            for food in foods:
                if allergen in food[1]:
                    if ingr_set is None:
                        ingr_set = set(food[0])
                    else:
                        ingr_set &= set(food[0])
            # If only 1 ingredient contains this allergen, add to the
            # dict of found allergen/ingredient combos
            if len(ingr_set) == 1:
                ingr = ingr_set.pop()
                found[allergen] = ingr
                is_found = True
                # Remove ingredient and allergen from all foods
                for food in foods:
                    if ingr in food[0]: food[0].remove(ingr)
                    if allergen in food[1]: food[1].remove(allergen)
                break
        # if we didn't find an allergen/ingredient, raise ValueError
        if not is_found:
            raise ValueError(f'no single ingredient found for any allergen')
    return [(ingr, aller) for aller,ingr in found.items()]

def sum_ingr_without_allergen(foods):
    '''
    Find the number of times all ingredients without an allergen appear
    in the sequence of foods.
    '''
    ingr_count = count_items(foods)
    ingr_with_allergen = [item[0] for item in ingredient_to_allergen(foods)]
    return sum(count for ingr,count in ingr_count.items() if ingr not in ingr_with_allergen)

def dangerous_ingr_list(foods):
    '''
    Return the output of ingredient_to_allergen() as a comma-separated
    list of ingredient names sorted by their allergens.
    '''
    ingr_to_aller = ingredient_to_allergen(foods)
    ingr_to_aller.sort(key=lambda item: item[1])
    return ','.join(item[0] for item in ingr_to_aller)

if __name__ == '__main__':
    foods = load_foods('input/day21.txt')
    # part 1
    print(sum_ingr_without_allergen(foods))
    # part 2
    print(dangerous_ingr_list(foods))
