from math import sqrt


def compute_func(n):
    return lambda x: x * n


def sort_dictionary(d, k=False):
    return dict(sorted(d.items(), key=lambda pair: str(pair[k])))


def sort_list_of_tuples(arr, k=0):
    return sorted(arr, key=lambda tup: tup[k])


car = {"model": "Ford",
       "year": 1984,
       "condition": "normal"}

print(sort_dictionary(car, True))
array = [(1, 8, 5), (9, 8, 6, 5, 4), (4, 5, 9, 2)]

min_len = len(min(*array, key=len))

for i in range(min_len):
    print(f"Перестановка кортежей по {i}-ому элементу кортежа: {sort_list_of_tuples(array, i)}")


print()
result = compute_func(5)
print(result(8))


find_gypot = lambda a, b: sqrt(a**2 + b**2)
out_find_gypot = lambda a, b: f"Гипотенуза треугольника с катетами {a} и {b} равна {find_gypot(a, b)}"

find_catet = lambda a, c: sqrt(c**2 - a**2)
out_find_gypot = lambda a, c: f"Катет треугольника с гипотенузой {c} и катетом {a} равен {find_catet(a, c)}"

print(out_find_gypot(12.34, 56.789))
print(out_find_gypot(4, 5))




