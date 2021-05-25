import json, random

def pick(meals, num):
    picked_meals = random.sample(sorted(meals), num)

    ingredients = set()
    names = list()

    for name in picked_meals:
        meal = meals[name]
        ingredients.update(meal['ingredients'])
        names.append(name)

    names.sort()
    ingredients = list(ingredients)
    ingredients.sort()
    
    return names, ingredients

def import_meals(filename):
    meals = json.loads(open(filename, 'r').read())
    return meals

def main():
    num = 4
    meals = import_meals('meals.json')
    names, ingredients = pick(meals, num)
    print(names)
    print(ingredients)

main()
