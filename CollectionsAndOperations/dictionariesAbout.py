
# Создание словаря и его заполнение (ключ: значение)
car = {
    "year": "1980",
    "brand": "Ford",
    "model": "Mustang",
}

# Используя метод .update можно в один словарь добавить содержимое другого словаря
car.update({"model": "Crown Victoria", "year": "1995", "miles": "153212"})
print(car)

# .value - получить значения словаря
print(car.values())
# .keys - получить ключи словаря
print(car.keys())

# В словаре мы обращаемся не по индексам, но по ключам. Здесь происходит вывод ключей и значений словаря
for key in car:
    # В каждой строке выведу "ключ" - "значение ключа"
    print(key, car[key], sep=" - ")

# Здесь функция сортировки словаря по значениям
def sort_dict_by_value(dict_to_sort):
    # Что происходит?
    # 1. Чтобы отсортировать коллекцию, воспользуюсь функцией sorted()
    # 2. В функцию sorted нужно положить коллекцию для сортировки.
    # Опционально: key - ключ, по которому буду сортировать; reverse - сортировать по возрастанию или убыванию
    # 3. Коллекцией будут выступать предметы словаря - .items сформирует элементы словаря как список пар ключ-значение
    # 4. В качестве ключа сортировки выберу значение, обозначу через lambda выражение, что это элемент пары по индексу 1
    # (индекс 0 - первый элемент, он же ключ; индекс 1 - второй элемент, оно же значение)
    # 5. Получился отсортированный список пар, преобразовываем обратно в словарь, обернув в dict()
    result = dict(sorted(dict_to_sort.items(), key=lambda pair: pair[1]))
    return result


words = {
    "Once": 3,
    "Some": 1,
    "Told": 5,
    "Body": 2,
    "Me": 6
}

print("Before sort by values:", words)
print("After sort by values:", sort_dict_by_value(words))

# telephone_book = {
#     "1234567": "Bob",
#     "1234765": "Alice",
#     "9876543": "Ron",
#     "1234567": "Richard"
# }
#
# for telephone_number in telephone_book:
#     print(f"Number {telephone_number} is connected with {telephone_book[telephone_number]}")

