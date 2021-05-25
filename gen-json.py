import json

meals = dict()

resp = 'y'

while resp == 'y':
    name = input('Meal name: ')
    ingredients = input('Ingredients (comma separated, all lowercase): ').split(', ')
    instructions = input('Instructions: ')

    meals[name] = {'ingredients': ingredients, 'instructions': instructions}

    resp = input('\nAdd another meal? [y/n]: ')

output = open('meals.json', 'w')
output.write(json.dumps(meals) + '\n')
