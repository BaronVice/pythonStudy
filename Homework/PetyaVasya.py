

def game_of_float(s: str) -> str:
    a, b = s.split()
    if a[0] != b[0]:
        return "Draw"

    len_a = len(a)
    len_b = len(b)
    if len_a == len_b:
        return "Draw"
    elif len_a > len_b:
        return "Petya won"
    else:
        return "Vasya won"


def game_of_range(s: str) -> str:
    a, b = map(int, s.split())

    petya = 0
    vasya = 0
    for number in range(a, b+1):
        if number % 3 == 0 or number % 8 == 0:
            petya += 1
        if number % 4 == 0 or number % 5 == 0:
            vasya += 1

    if petya == vasya:
        return "Draw"
    elif petya > vasya:
        return "Petya won"
    else:
        return "Vasya won"


def game_of_numbers(n: int):
    positive = 0
    negative = 0
    zeros = 0

    multiplication = 1
    for _ in range(n):
        number = int(input())
        if number < 0:
            negative += 1
        elif number > 0:
            positive += 1
        else:
            zeros += 1

        multiplication *= number

    print(positive, negative, sep=' ')
    print(multiplication, end=' ')
    if zeros:
        print("positive")
    elif negative % 2:
        print("negative")
    else:
        print(positive)


