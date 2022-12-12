from math import sqrt


def is_even(n: int):
    return "even" if n % 2 == 0 else "odd"


number = 12.123
digit = 5
name = "John"

nickname = " Doe"

# print(number + digit)
# print(name + nickname)
#
# print(type(number))
# number = str(number)
# print(type(number))

# Цикл for определяет, делится ли число на 7.
# И если да, то выводит его
for num in range(1, 30):
    if num % 7 == 0:
        print(f"{num} can be divided by 7")
    print("End of if block")
print("End of for block")


"""
--- Типы данных ---
Текстовые: str 
Числовые: int, float, complex
Последовательности: list, tuple, range
Отображаемый: dict
Множества: set, frozenset
Логический: bool
"""

array = []
mn = set()
for i in range(1, 7):
    array.append(i)
    mn.add(i)

s = """Lorem ipsum dolor sit amet,
        consectetur adipiscing elit,
            sed do eiusmod tempor incididunt
                ut labore et dolore magna aliqua."""

message = "banana"
for char in message:
    print(char)

string = "aboba"
sub_string = "baa"

if sub_string in string:
    print(f"substring {sub_string} exists in string {string}")
else:
    print(f"substring {sub_string} not exists in string {string}")

print(message[-5:-1:])

message = "Random words in string"
print(len(message))


print(is_even(8))




