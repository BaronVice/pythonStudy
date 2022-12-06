

def greetings(name="пользователь"):
    return "Привет, " + name


def factorial(n):
    result = 1
    for number in range(2, n+1):
        result *= number
    return result


def filter_even(arr):
    return [number for number in arr if number % 2 == 0]


def filter_unique(arr):
    unique_arr = []
    for element in arr:
        if element not in unique_arr:
            unique_arr.append(element)
    return unique_arr


array = [1, 2, 3, 3, 3, 3, 4, 5]
unique_values = filter_unique(array)

print(array, unique_values, sep="\n")