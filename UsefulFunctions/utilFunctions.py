

def multiple_numbers(first_number, *numbers):
    result = first_number
    for number in numbers:
        result *= number

    return result


def sum_of_three(numbers):
    if len(numbers) < 3:
        return

    result = []
    for i in range(2, len(numbers)):
        result.append(numbers[i - 2] + numbers[i - 1] + numbers[i])

    return result


def multiple_of_three(a, b, c):
    return a * b * c


def pow_numbers(arr, n):
    result = list(map(lambda el: el**n, arr))
    return result


array = [2, 4, 6, 8, 9, 15]
print(pow_numbers(array, 6))

even = list(filter(lambda el: el % 2 == 0, array))
print(even)



