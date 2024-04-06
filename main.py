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


def get_shop_list_by_dishes(dishes: list, person_count: int) -> dict:
    shop_list = {}
    for dish in dishes:
        for position in cook_book[dish]:
            shop_lists_ingredient = {'measure': position['measure'], 'quantity': position['quantity'] * person_count}
            shop_list[position['ingredient_name']] = shop_lists_ingredient
    return shop_list


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
print('cook_book: ', cook_book)
dishes = ['Запеченный картофель', 'Омлет']
person_count = 2
shop_list_for_dishes = get_shop_list_by_dishes(dishes, person_count)
print('shop list for disher: ', shop_list_for_dishes)
files_name = ['1.txt', '2.txt', '3.txt']
files_data = []
for name in files_name:
    file = open(name, encoding='UTF-8')
    files_data.append(file.readlines())
    file.close()
files_list = list(zip(files_name, files_data))
sorted_files_list = sorted(files_list, key=lambda x: len(x[1]))
with open('union_file', 'w', encoding='UTF-8') as result_file:
    for file in sorted_files_list:
        result_file.write(file[0] + '\n')
        result_file.write(str(len(file[1])) + '\n')
        result_file.write(''.join(file[1]) + '\n')