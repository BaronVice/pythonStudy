# Список (list) - изменяемая коллекция
# Нужный выбор, если нам нужна коллекция, в которой будем добавлять/удалять/изменять элементы

# Так создается список
a = [1, 3, 4, 7]
# Или использую функцию list() можно преобразовать какой-то объект в список
# a = list((1, 3, 4, 7))

# Добавляем элемент в конец списка
a.append(2)
print(a)

# Расширяем список, добавляя несколько элементов в конец списка
a.extend([5, 6, 20])
print(a)

# Вставляем на 0-ой элемент значение 9
a.insert(0, 9)
print(a)

# Удаляем первый встреченный элемент по значению
a.remove(9)
print(a)

# Удаляем элемент по индексу и получаем его значение
a.pop(-1)   # -1 означает первый элемент с конца
print(a)

# Считаем количество встреченных элементов в списке
a.count(1)
print(a)

# Сортируем список
a.sort()
print(a)
