given_string = "1 - 2 - 3 - 4 - 5"
print("List before split: ", given_string)
# Метод .split вернет список из элементов строки, разбитых по разделителю
print("List after split: ", list(map(int, given_string.split(" - "))))

given_string = (123, "456", 0.5)
# Метод .join преобразует коллекцию в строку, объединив элементы по заданному соединителю
print("Tuple after join: ", " : ".join(str(el) for el in given_string))

given_string = "-----------------a-b-o-b-a------------"
# Метод .strip удалит все заданные символы слева и справа, пока не встретится другой символ
print("String after strip: ", given_string.strip("-"))
# Метод .replace заменит старый символ на новый столько раз, сколько укажем (не укажем - заменит все вхождения)
print("String after replace: ", given_string.replace("-", "Start", 1))
print()

given_string = "123abc"
print(given_string)
# .isalpha - проверит, содержит ли строка только буквы
print("only letters") if given_string.isalpha() else print("not only letters")
# .isdigit - проверит, содержит ли строка только цифры
print("only digits") if given_string.isdigit() else print("not only digits")
# .isnumeric - проверит, содержит ли строка только числа (сюда также входят дробные числа в один символ и римские числа)
print("is number") if given_string.isnumeric() else print("is not number")
# .isalnum - проверит, содержит ли строка только буквы и числа
print("only letters and numbers") if given_string.isalnum() else print("not only letters and numbers")
print()

given_string = "abobabobab"
# Метод .find вернет первое слева вхождение подстроки в строке, если не найдет, то вернет -1
print(given_string.find('bab'))
# Метод .index работает как find, но если вхождение не найдено выкинет ошибку
print(given_string.index("bab"))
print()

given_string = "YER, wizard Harry"
# Метод .startswith проверит, начинается ли строка с заданной подстроки
print("Starts with our value: ", (given_string.lower()).startswith("yer"))
# Метод .endswith проверит, заканчивается ли строка на заданную подстроку
print("Ends with our value: ", given_string.endswith("a"))
print()

given_string = "sOme bOdy oNce tOlD mE"
# Метод .lower переведет все символы строки в нижний регистр
print("given_string after .lower: ", given_string.lower())
# Метод .upper переведет все символы строки в верхний регистр
print("given_string after .upper: ", given_string.upper())
# Метод .title сделает каждую первую букву слова в верхнем регистре, остальные буквы слова в нижнем
print("given_string after .title: ", given_string.title())
# Метод .capitalize сделает первую букву строки в верхнем регистре, остальные переведет в нижний
print("given_string after .capitalize: ", given_string.capitalize())
print()

given_string = given_string.lower()
# Методд .count посчитает количество непересекающихся вхождений подстроки в строку
print("given_string .count(me): ", given_string.count("me"))
