from random import randint
from functionsCreation import generate_random_list


# Функция сравнения трех чисел, из которых вернет максимальное
def max_of_three(first_number, second_number, third_number):
    if first_number <= second_number and third_number <= second_number:
        return second_number
    elif first_number <= third_number and second_number <= third_number:
        return third_number
    else:
        return first_number


# Функция, которая посчитает сумму элементов коллекции
def sum_of_array(collection):
    result = 0
    for element in collection:
        result += element
    return result


# Эта функция посчитает произведение чисел в коллекции
def multiply_of_array(collection):
    if len(collection) == 0:
        return 0

    result = 1
    for element in collection:
        result *= element
    return result


# Здесь развернем последовательность
def reverse_array(collection):
    return collection[::-1]


array = generate_random_list(10, 30, 3, 3)
print(array)
print(max_of_three(*array))

print()

array = generate_random_list(-30, 60, 3, 6)
print(array)
print(sum_of_array(array))
print(multiply_of_array(array))

print()

print(array)
print(reverse_array(array))

