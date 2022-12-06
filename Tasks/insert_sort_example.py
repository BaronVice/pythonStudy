from random import randint
from time import time


def insertion_sort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > temp:
            arr[j + 1] = arr[j]
            arr[j] = temp
            j -= 1


array = [randint(-100, 100) for _ in range(10000)]
#print("Before: ", *array)
start = time()

insertion_sort(array)

#print("After: ", *array)
end = time()
print(end - start)