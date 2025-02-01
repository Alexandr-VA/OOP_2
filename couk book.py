def get_shop_list_by_dishes(dishes, person_count):

    '''Чтение из файла и воссоздание словаря'''

    with open('cook_book.txt', 'r') as file:
        text = file.read()
        text = "\n".join(text.split("\n")[1:-1])
        names = []
        dish_book = {}

        for txt in text.split('\n\n'):
            recipe = []
            name, n, *args = txt.split('\n')
            names.append(name.strip())

            for arg in args:
                ingredient_name, quantity, measure = map(lambda x: int(x) if x.isdigit() else x, arg.split(' | '))
                recipe.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
            dish_book[name.strip()] = recipe

    '''Расчёт ингредиентов нескольких блюд для нескольких клиентов'''

    ingredients = {}
    for dish in dishes:
        if dish in dish_book:
            for ingr in dish_book[dish]:
                if ingr['ingredient_name'] in ingredients:
                    ingredients[ingr['ingredient_name']]['quantity'] += ingr['quantity'] * person_count
                else:
                    ingredients[ingr['ingredient_name']] = {'measure': ingr['measure'], 'quantity': \
                    int(ingr['quantity']) * person_count}
        else:
            print(f'Такого блюда в меню нет')
    for name, measure in ingredients.items():
        print(f'{name}: {measure}')


'''Вызов функции'''

get_shop_list_by_dishes(['Омлет', 'Омлет', 'Фахитос'], 2)
