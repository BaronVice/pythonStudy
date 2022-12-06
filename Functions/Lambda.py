

def some_func():
    print("Inside function")


def set_number_in_power(number, power=2):

    result = number ** power
    print("First check")
    return result


def find_first_even(arr):

    for number in arr:
        if number%2 == 0:
            return number

    return -1


some_func()
print("Outside function")
print()

array = [5, 1, 7, 3, 9]
# Используя лямбда-выражения можно писать короткие функции, которые удобно использовать в других функциях
# Например в сортировке пар можно через лямбду указать по какому элементу пары хотим сортировать
# lambda pair: pair[0]

# Сперва объявим lambda, далее укажем какие аргументы используем, затем пропишем, что лямбда будет делать,
# После чего, откуда она будет брать аргументы для исполнения
print(list((lambda num: num**2)(el) for el in array))




