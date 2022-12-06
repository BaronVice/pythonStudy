# Это список (list) - с ним можно делать что угодно
arr_list = [1, 2, 3, 3, 3]
print(arr_list)

# Это строка (string или в питоне str) - она неизменяема и хранит в себе символы
word = "something"
# Это как она примерно выглядит (массив символов)
print(list(word))

# Кортеж (tuple) - неизменяемая коллекция (статическая), но работает быстрее списка (динамический)
arr_tuple = (1, 2, 3, 3, 3)
print(arr_tuple)

# Используя такие функции можно преобразовывать коллекции из одного типа в другой
print(list(arr_tuple))
print(tuple(arr_list))

# Множества set - хранят в себе уникальные элементы, при этом у них нет индексирования (всегда разбросаны)
arr_set = {1, 2, 3, 3, 3, 4}
# Каждый раз порядок при выводе будет другой
for _ in range(5):
    print(arr_set)

# Это тоже set, но статический - нельзя добавлять/удалять/изменять элементы, но работает быстрее обычного
arr_frozen_set = frozenset({1, 2, 3, 3, 3, 4})

# Словарь (dict) - хранит в себе пары "ключ : значение",
# где ключ - не изменяем и уникален, а значение может быть любым и изменяться
countries = {
            "Russia" : "Moscow",
             "Germany" : "Berlin",
             "Japan" : "Tokyo"
             }




