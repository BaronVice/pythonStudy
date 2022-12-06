arr = {}
# У каждого объекта есть свой тип, его можно узнать используя функцию type()
print(type(arr))
# Создание множества
arr = {1, 2, 3, 3, 3, 4, 5}
print(arr)

# В множество можно добавить объект
arr.add(7)
print(arr)

# Или удалить его по значению
arr.remove(1)       # Если элемент не найден, будет вызвано исключение
# arr.discard(5)    # Если не хотим обрабатывать исключения, то можно использовать аналогичный
                    # метод discard(). В отличии от .remove() он не выкидывает исключение
print(arr)

# Или удалить по индексу
el = arr.pop()      # В данном случае удаляем последний элемент и получаем его значение
print(el, arr)

first_set = {1, 5, 6, 8}
second_set = {3, 1, 6}
# Можно узнать разницу двух множеств (какие элементы)
# В данном случае спрашиваем, какие элементы первого множества не содержатся во втором
result = first_set.difference(second_set)
print(result)

# Можно объединить два множества в одно
result = first_set.union(second_set)
print(result)

# Или добавить в первое множество элементы второго
first_set.update(second_set)
print(first_set)

