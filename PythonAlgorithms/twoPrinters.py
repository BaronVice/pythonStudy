from math import ceil
from math import floor

# def find_time(n, x, y):
#     return n * x * y / (x+y)
#
#
# n, x, y = map(int, input().split())
# result = min(x,y)
# n -= 1
# result += ceil(find_time(n, x, y))
# print(result)
#
# # Считаем t для определения количества напечатанных страниц каждого принтера
# def optimal(n, x, y):
#     return n * x * y / (x+y)
#
#
# def find_time(n, x, y):
#     opt = optimal(n, x, y)
#     #print(opt)
#     first_case_X = floor(opt/x)         # сколько листов напечатает x в первом случае
#     first_case_Y = n - first_case_X     # сколько листов напечатает y в первом случае
#     #print(first_case_X, first_case_Y)
#     # Время в первом случае - выбор времени того принтера, который последним закончит свою работу
#     first_case_time = max(y * first_case_Y, x * first_case_X)
#
#     second_case_X = ceil(opt/x)         # сколько листов напечатает x во втором случае
#     second_case_Y = n-second_case_X     # сколько листов напечатает y во втором случае
#     #print(second_case_X, second_case_Y)
#     # Время во втором случае - выбор времени того принтера, который последним закончит свою работу
#     second_case_time = max(y * second_case_Y, x * second_case_X)
#
#     # Оба решения будут рабочими, но по условию нужно выбрать минимальное
#     return min(first_case_time, second_case_time)
#
#
# n, x, y = map(int, input().split())
# result = min(x,y)
# n -= 1
# result += find_time(n, x, y)
# print(result)


def find_optimal_time(n, x, y):
    return x * y * n / (y + x)


def find_time(n, x, y):
    optimal = find_optimal_time(n, x, y)
    first_case_x = ceil(optimal / x)
    first_case_y = n - first_case_x
    first_case_time = max(first_case_x * x, first_case_y * y)

    second_case_x = floor(optimal / x)
    second_case_y = n - second_case_x
    second_case_time = max(second_case_x * x, second_case_y * y)

    return min(first_case_time, second_case_time)


n, x, y = map(int, input().split())
n -= 1
print(find_time(n, x, y) + min(x, y))