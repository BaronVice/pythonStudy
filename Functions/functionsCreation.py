from random import randint

# def "название функции"("аргумент1", "аргумент2", ..., "аргументN"):
#   функция что-то делает
#   return что-то (опционально)


def generate_random_list(low_value=-100, high_value=100, low_quantity=10, high_quantity=30):
    generated_list = [randint(low_value, high_value) for _ in range(randint(low_quantity, high_quantity))]
    return generated_list


def array_out_len_min_max(array):
    print(min(array), max(array), len(array))
    print(*array)


def fib(n):
    if n == 1 or n == 2:
        return 1

    return fib(n - 1) + fib(n - 2)