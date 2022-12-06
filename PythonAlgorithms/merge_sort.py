from random import randint
from time import time

from math import ceil


def merge_sort(arr):
    if len(arr) < 2:
        return

    mid = ceil(len(arr)/2)

    left_half = arr[:mid]
    right_half = arr[mid:]

    merge_sort(left_half)
    merge_sort(right_half)

    merge(arr, left_half, right_half )


def merge(arr, left_half, right_half):
    left_size = len(left_half)
    right_size = len(right_half)

    i, j, k = 0, 0, 0
    while i < left_size and j < right_size:
        if left_half[i] <= right_half[j]:
            arr[k] = left_half[i]
            i += 1
        else:
            arr[k] = right_half[j]
            j += 1
        k += 1
    while i < left_size:
        arr[k] = left_half[i]
        i += 1
        k += 1
    while j < right_size:
        arr[k] = right_half[j]
        j += 1
        k += 1


array = [randint(-100, 100) for _ in range(100000000)]
print("Before: ", *array)
# start = time()

merge_sort(array)
print("After: ", *array)
# stop = time()
# print(stop - start)

