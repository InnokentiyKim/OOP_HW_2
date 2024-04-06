cook_book = {}


def get_recipes_lists(all_data: list) -> list:
    all_recipes = []
    recipe_ = []
    for ind, line in enumerate(all_data):
        if line != '\n' and ind < len(all_data) - 1:
            recipe_.append(line.strip())
        elif ind == len(all_data) - 1:
            recipe_.append(line.strip())
            all_recipes.append(recipe_)
        else:
            all_recipes.append(recipe_)
            recipe_ = []
    return all_recipes

def get_components(component: str) -> list:
    true_component = component.split(' | ')
    true_component[1] = int(true_component[1])
    return true_component


with open('recipes.txt', encoding='UTF-8') as recipes_file:
    all_data = recipes_file.readlines()
    all_recipes = get_recipes_lists(all_data)

for recipe in all_recipes:
    dish = recipe[0]
    ingredients_count = int(recipe[1])
    ingredients_list = []
    ingredients_title = ['ingredient_name', 'quantity', 'measure']
    for i in range(ingredients_count):
        components = get_components(recipe[2 + i])
        ingredient = dict(zip(ingredients_title, components))
        ingredients_list.append(ingredient)
    cook_book[dish] = ingredients_list

    
        

