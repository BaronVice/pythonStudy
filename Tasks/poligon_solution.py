n = int(input())
array = list(map(int, input().split()))
numbers = [el for el in range(1, n + 2)]

array.sort()
i = 0
for el in array:
    if el == numbers[i]:
        i += 1
    else:
        break
print(numbers[i])