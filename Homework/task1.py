""" Это разбор пяти задач с занятия по функциям """


# Функция сравнения двух чисел
def compare_two_numbers(s: str):
    a, b = map(int, s.split())
    if a > b:
        return "a is better"
    if a < b:
        return "b is better"
    return "equal"


# Функция формирования четных чисел в заданном диапазоне
def even_numbers(s: str):
    start, stop = map(int, s.split())
    even = [num for num in range(start, stop+1) if num % 2 == 0]
    return even


# Здесь мы проверяли число на правильную последовательность
def is_correct(number: int):
    num = str(number)
    if len(num) == 1:
        return "Correct"

    for i in range(len(num)-1):
        if int(num[i]) - 1 != int(num[i+1]):
            return "Incorrect"

    return "Correct"


# Определяем, есть ли в строке пятерки, и если есть, то в каком количестве
def find_five(s: str):
    cnt = s.count('5')
    if cnt:
        # Да, в python'е для return'а можно указать несколько значений
        return "Yes", cnt
    else:
        return "No", ''


# Составляем топливо для прибора
def fuel(num: int):
    # В задаче требовалось вернуть список из чисел, здесь можно обойтись вложенным списком
    return [el for el in range(123, 457) if el % num == 0]


print(compare_two_numbers('7 3'))
print(compare_two_numbers('7 13'))
print(compare_two_numbers('7 7'))
print()

print(*even_numbers('3 19'))
print()

print(is_correct(5432))
print(is_correct(678))
print(is_correct(9))
print(is_correct(7128))
print(is_correct(9876543210))
print()

print(*find_five('sdfffs'), sep='\n')
print(*find_five('5gfdsg5sf5'), sep='\n')
print()

print(fuel(5))
print(fuel(9))


