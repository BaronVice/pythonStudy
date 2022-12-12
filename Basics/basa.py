from math import sqrt


def is_even(n: int):
    return "even" if n % 2 == 0 else "odd"


def list_occurrences(first_list: list, second_list: list) -> list:
    """ Вернет список, состоящий из элементов second_lst, что входят в first_lst """
    return [el for el in second_list if el in first_list]


def list_filter_string(given_list: list, letter: str) -> list:
    """ Вернет список из элементов given_list, что содержат в себе букву letter """
    result = []
    for el in given_list:
        if letter in el:
            result.append(el)

    return result


number = 12.123
digit = 5
name = "John"

nickname = " Doe"

# print(number + digit)
# print(name + nickname)
#
# print(type(number))
# number = str(number)
# print(type(number))

# Цикл for определяет, делится ли число на 7.
# И если да, то выводит его
for num in range(1, 30):
    if num % 7 == 0:
        print(f"{num} can be divided by 7")
#   Конец блока if
# Конец блока for


"""
--- Типы данных ---
Текстовые: str 
Числовые: int, float, complex
Последовательности: list, tuple, range
Отображаемый: dict
Множества: set, frozenset
Логический: bool
"""

array = []
mn = set()
for i in range(1, 7):
    array.append(i)
    mn.add(i)

s = """Lorem ipsum dolor sit amet,
        consectetur adipiscing elit,
            sed do eiusmod tempor incididunt
                ut labore et dolore magna aliqua."""

message = "banana"
for char in message:
    print(char)

string = "aboba"
sub_string = "baa"

if sub_string in string:
    print(f"substring {sub_string} exists in string {string}")
else:
    print(f"substring {sub_string} not exists in string {string}")

print(message[-5:-1:])

message = "Random words in string"
print(len(message))


print(is_even(8))
print('\n\n')

# Список: в нем предметы упорядоченны, элементы изменяемы, возможны повторения значения
array = [123, 456, 'some_string', True, False, ('a', 2), True]
array[0] += array[1]
array.append(567)
array.remove(True)
print(array)
print(len(array))
print(isinstance(array, tuple))

fruits = list(("apple", "banana", "orange", "melon", "grape"))
print(fruits[-1])
print(fruits[3:])
print(fruits)
fruits[1:4] = ["watermelon", "cherry"]
print(fruits)

fruit = "orange"
if fruit in fruits:
    print(f"{fruit} exists in fruits")
else:
    print(f"{fruit} doesn't exist in fruits")

print(fruits)
fruits.append("ginger")
print(fruits)
fruits.insert(0, "orange")
print(fruits)

products = ["chocolate", "cake", "soda"]
products.extend(fruits)
print(products)

products.remove("cake")
print(products)

deleted_product = products.pop(5)
print(deleted_product)
print(products)

del products[4]
print(products)

# Синтаксис вложенных списков:
# [ВЫРАЖЕНИЕ for ПРЕДМЕТ in КОЛЛЕКЦИЯ if УСЛОВИЕ == True]

# products_with_o = []
# for product in products:
#     if 'o' in product:
#         products_with_o.append(product)

products_with_o = list_filter_string(products, 'o')
products_with_a = list_filter_string(products, 'a')
print()
print(products_with_o)
print(products_with_a)
new_list = list_occurrences(products_with_a, products_with_o)
print(new_list)

# for product in products:
#     print(product)

# [print(product) for product in products]


