# Разбивает строку на части, используя разделитель, и возвращает эти части списком
given_string = "1 - 2 - 3"
print(given_string.split(" - "))

# Возвращает строку, собранную из элементов указанной коллекции
given_string = "123"
print(" - ".join(given_string))

# Возвращает копию указанной строки, с обоих концов которой устранены указанные символы
given_string = "aboba "
print(given_string.strip(" "))

# Содержит ли строка только буквы
print("abcdefфбвш".isalpha())
print("abc def".isalpha())
# Содержит ли строка только цифры
print("123".isdigit())
print("-123".isdigit())
# Содержит ли строка только числа
print("⅓".isnumeric())
print("Ⅻ".isnumeric())
# Содержит ли строка только чисел и буквы
print("123abc".isalnum())
print("123⅓dsa".isalnum())

# возвращает количество непересекающихся вхождений в неё указанной подстроки.
given_string = "abobabababa"
print(given_string.count("baba"))

# Возвращает наименьший индекс, по которому обнаруживается начало указанной подстроки в исходной
given_string = "weird things things"
print(given_string.find("thing"))
print(given_string.find("oi"))
# То же, что и выше, но...
print(given_string.index("thing"))
# print(given_string.index("oi"))

# Возвращает переменную типа bool, начинается ли строка с заданной строки
given_string = "Yer a wizard, Harry"
print(given_string.startswith("Y"))
print(given_string.startswith("Harry"))
# Возвращает переменную типа bool, заканчивается ли строка на заданную строки
print(given_string.endswith("arry"))
print(given_string.endswith("wizard"))

# Возвращает копию строки, делая первую букву заглавной
given_string = "sOme bOdy oNce tOlD mE"
print(given_string.capitalize())

# Возвращает копию строки, в которой каждое новое слово начинается с заглавной буквы и продолжается строчными
given_string = "sOme.bOdy, oNce-tOlD mE"
print(given_string.title())

# Возвращает копию исходной строки с символами приведёнными к верхнему регистру
given_string = "sOme bOdy oNce tOlD mE"
print(given_string.upper())
# Возвращает копию исходной строки с символами приведёнными к нижнему регистру
given_string = "sOme bOdy oNce tOlD mE"
print(given_string.lower())

# Возвращает копию строки, в которой заменены все вхождения указанной строки заданным значением
given_string = "He is suspicious person"
print(given_string.replace("suspicious person", "sus"))
print(given_string.replace("s", "S", 1))
