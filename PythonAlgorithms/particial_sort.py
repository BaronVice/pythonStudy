from random import randint

n = int(input())
array = [randint(0, 1000) for _ in range(n)]

max_value = max((array)) + 1

count_values = [0] * max_value

for element in array:
    count_values[element] += 1

print(*array)

for i in range(max_value):
    if count_values[i] != 0:
        for j in range(count_values[i]):
            print(i, end=' ')