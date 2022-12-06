array = [3, 4, "some string", 9, 4, 2, 4]
print(array)

# Добавление элемента в конец списка
element = input("Введите элемент, для добавления в конец списка: ")
array.append(element)
print(array)

# Добавление нескольких элементов
s = input("Введите несколько целочисленных элементов через пробел, для добавления в конец списка: ")
elements = list(map(int, s.split()))
array.extend(elements)
print(array)

# Добавление элемента на заданную позицию
s = input("Введите через пробел позицию и элемент, который вы хотите добавить в список: ")
i, element = s.split()
array.insert(int(i), element)
print(array)

# Считаем количество заданных элементов в списке
element = int(input("Введите целое число для поиска: "))
occurrences = array.count(element)
print(occurrences)

# Ищем индекс первого встреченного элемента на отрезке
s = input("Введите элемент для поиска, индексы начала и конца отрезка: ")
elements = list(map(int, s.split()))
found_index = array.index(elements[0], elements[1], elements[2])
print(found_index)

# Удаляем элемент по индексу
i = int(input("Введите индекс для удаления элемента: "))
deleted_element = array.pop(i)
print(deleted_element, array)

# Удаляем элемент по значению
element = int(input("Введите целое число для удаления: "))
array.remove(element)
print(array)

# Переворачиваем список
array.reverse()
print(array)

# Сортируем список
array = list(map(str, array))
array.sort(key=len, reverse=True)
print(array)
array.sort(key=len, reverse=False)
print(array)

# Копируем элементы списка
copy_array = array.copy()
array.extend([1, 2, 3, 4])
print(array, copy_array, sep="\n")
