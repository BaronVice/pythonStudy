from random import randint
from time import time


def insertion_sort(arr):
    for i in range(1, len(arr)):
        current_value = arr[i]
        position = i - 1
        while position >= 0 and arr[position] > current_value:
            arr[position + 1] = arr[position]
            arr[position] = current_value
            position -= 1


array = [randint(-100, 100) for _ in range(10000)]
# print("Before: ", *array)
start = time()

insertion_sort(array)

# print("After: ", *array)
end = time()
print(end - start)