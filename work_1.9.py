# coding: utf-8


def read_file():
    cook_book = {}
    with open('menu.txt', 'r', encoding='utf-8') as file:
        for line in file:
            dish_name = line.strip().lower()  # создаем переменную "название блюда", убираем пустую строку, делаем нижний регистр
            list_ingridient_name = []  # новый список ингридиентов
            count_ingridient = file.readline().strip()  # количество ингридентов в одном блюде, убираем пробелы
            for name in range(int(count_ingridient)):
                name = file.readline().split(' | ') # добавляем разделитель
                list_ingridient_name.append(
                    {'ingridient_name': name[0].strip().lower(),
                     'quantity': int(name[1]),
                     'measure': name[2].strip()})
                cook_book[dish_name] = list_ingridient_name
            file.readline()
        return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    cook_book = read_file()
    for dish in dishes:
        for ingridient in cook_book[dish]:
            new_shop_list_item = dict(ingridient)

            new_shop_list_item['quantity'] *= person_count
            if new_shop_list_item['ingridient_name'] not in shop_list:
                shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
            else:
                shop_list[new_shop_list_item['ingridient_name']]['quantity'] += new_shop_list_item['quantity']

    return shop_list


def print_shop_list(shop_list):
    for shop_list_item in shop_list.values():
        print(
            '{} {} {}'.format(shop_list_item['ingridient_name'], shop_list_item['quantity'], shop_list_item['measure']))


def create_shop_list():
    person_count = int(input('Введите количество человек: '))
    dishes = input('Введите блюда в расчете на одного человека (через запятую): ').lower().split(', ')
    # cook_book[dish] = read_file()
    shop_list = get_shop_list_by_dishes(dishes, person_count)
    print_shop_list(shop_list)


create_shop_list()

# Задача №2
# Напишите, для чего используются типы данных: json, xml, yaml.
# JSON (англ. JavaScript Object Notation) — текстовый формат обмена данными, основанный на JavaScript и обычно используемый именно с этим языком.
# Формат считается языконезависимым и может использоваться практически с любым языком программирования.
#  var earth =
# {
#  "planet" :
#  {
#   "name" : "earth",
#   "type" : "small",
#   "info":
#   [
#    "Earth is a small planet, third from the sun",
#    "Surface coverage of water is roughly two-thirds",
#    "Exhibits a remarkable diversity of climates and landscapes"
#   ]
#  }
#  };

# xml
# XML – это eXtensible Markup Language, что в переводе значит «расширенный язык разметки».
# Фактически, это способ записи данных в структурированном виде, который будет читаем для пользователя,
# но при этом удобен для обработки программному обеспечению. XML документ содержит один или более элементов,
#  разделённых открывающими и закрывающими тегами:

# <str>Hello!</str>

# YAML — легкочитаемый формат сериализации данных, концептуально близкий к языкам разметки,
# но ориентированный на удобство ввода-вывода типичных структур данных многих языков программирования.

# ---
#  -
#     - PRIVMSG
#     - newUri
#     - '^http://.*'
#  -
#     - PRIVMSG
#     - deleteUri
#     - ^delete.*
#  -
#     - PRIVMSG
#     - randomUri
#     - ^random.*