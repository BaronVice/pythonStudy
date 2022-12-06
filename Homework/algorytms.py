""" Задачи на функции """


# Вернет состав строки
def check_states(given_string: str):
    if given_string.isdigit():
        return "Digits only"
    if given_string.isalpha():
        return "Letters only"
    if given_string.isalnum():
        return "Letters and digits"

    return "Weird string"


# Переведет в строке буквы из верхнего регистра в нижний и наоборот
def swap_cases(given_string: str):
    return ''.join([letter.upper() if letter.islower() else letter.lower() for letter in given_string])


# Замена пробелов между словами на дефис
def split_and_join(given_string: str):
    new_string = given_string.strip()
    new_string = new_string.replace(' ', '-')
    return new_string


# Посчитаем среднюю высоту растений
def flowers_average(heights_of_flowers):
    return sum(heights_of_flowers) / len(heights_of_flowers)


# Так можно было решить задачу на подсчет подстроки
def count_substrings(string: str, substring: str):
    counter = 0
    for i in range(0, len(string)-len(substring)+1):
        if substring == string[i:i+len(substring)]:
            counter += 1
        print(substring, string[i:i+len(substring)])
    return counter


print(count_substrings("abcdcdcdc", "cdc"))
