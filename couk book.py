''' Книга рецептов'''

cook_book = {
  'Омлет': [
    {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт'},
    {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
    {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
    ],
  'Утка по-пекински': [
    {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
    {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
    {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
    {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
    ],
  'Запеченный картофель': [
    {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
    {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
    {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
    ],
  'Фахитос': [
    {'ingredient_name': 'Говядина', 'quantity': 500, 'measure': 'г'},
    {'ingredient_name': 'Перец сладкий', 'quantity': 1, 'measure': 'шт'},
    {'ingredient_name': 'Лаваш', 'quantity': 2, 'measure': 'шт'},
    {'ingredient_name': 'Винный уксус', 'quantity': 1, 'measure': 'ст.л'},
    {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
    ]
  }

'''Создание списка рецептов и запись в файл: cook_book.txt'''

with open('cook_book.txt','w') as file:
    for name, ingrid in cook_book.items():
#        print(f'\n{name}\n{len(ingrid)}')      # проверка кода
        file.write(str((f'\n{name} \n{len(ingrid)}')) + '\n')
        for element in ingrid:
#            print(*list(element.values()), sep =' | ')     # проверка кода
            element_values_str = " | ".join(map(str, list(element.values())))
            file.write(element_values_str + '\n')


def get_shop_list_by_dishes(dishes, person_count):

    '''Чтение из файла и воссоздание словаря'''

    with open('cook_book.txt', 'r') as file:
        text = file.read()
        text = "\n".join(text.split("\n")[1:])
        text = "\n".join(text.split("\n")[:-1])
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
    for dish, ingrid_list in dish_book.items():
        for i in dishes:
            if dish == i:
                for ingr in ingrid_list:
                    ingredients[ingr['ingredient_name']] = {'measure': ingr['measure'], 'quantity': int(ingr['quantity'])*\
                    person_count}
                    
    for name, measure in ingredients.items():
        print(f'{name}: {measure}')


'''Вызов функции'''

get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
