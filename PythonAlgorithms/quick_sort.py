from random import randint
from time import time


def quick_sort(array, low, high):

    if low > high:
        return

    pivot = array[high]

    left_pointer = low
    right_pointer = high

    while left_pointer < right_pointer:
        while array[left_pointer] <= pivot and left_pointer < right_pointer:
            left_pointer += 1;
        while array[right_pointer] >= pivot and left_pointer < right_pointer:
            right_pointer -= 1;
        array[left_pointer], array[right_pointer] = array[right_pointer], array[left_pointer]

    array[left_pointer], array[high] = array[high], array[left_pointer]

    quick_sort(array, low, left_pointer-1)
    quick_sort(array, left_pointer+1, high)


n = int(input())
array = [randint(-100, 100) for _ in range(n)]
print("Before: ", *array)

quick_sort(array, 0, n-1)
print("After: ", *array)
