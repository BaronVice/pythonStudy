from random import randint
from time import time

from math import ceil


def merge_sort(arr):

    if len(arr) < 2:
        return

    mid = ceil(len(arr) / 2)

    left_half = arr[:mid]
    right_half = arr[mid:]

    merge_sort(left_half)
    merge_sort(right_half)

    merge(arr, left_half, right_half)


def merge(arr, left_half, right_half):
    left_length = len(left_half)
    right_length = len(right_half)

    i, j, k = 0, 0, 0
    while i < left_length and j < right_length:
        if left_half[i] <= right_half[j]:
            arr[k] = left_half[i]
            i += 1
        else:
            arr[k] = right_half[j]
            j += 1
        k += 1
    while i < left_length:
        arr[k] = left_half[i]
        i += 1
        k += 1
    while j < right_length:
        arr[k] = right_half[j]
        j += 1
        k += 1


def insertion_sort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > temp:
            arr[j + 1] = arr[j]
            arr[j] = temp
            j -= 1


array1 = [randint(-100, 100) for _ in range(100000)]
# print("Before: ", *array)
start = time()

merge_sort(array1)

# print("After: ", *array)
stop = time()
print("Merge sort time:  ", stop - start)

array2 = [randint(-100, 100) for _ in range(100000)]
start = time()

insertion_sort(array2)

stop = time()
print("Insert sort time: ", stop - start)