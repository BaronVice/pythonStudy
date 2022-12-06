
n = int(input())

array = tuple(map(int, input().split()))
array_prefix = [0]
for i in range(n):
    array_prefix.append(array_prefix[i] + array[i])

array_sorted = sorted(array)
array_sorted_prefix = [0]
for i in range(n):
    array_sorted_prefix.append(array_sorted_prefix[i] + array_sorted[i])

m = int(input())
for i in range(m):
    request, left, right = map(int, input().split())

    if request == 1:
        print(array_prefix[right] - array_prefix[left - 1])
    else:
        print(array_sorted_prefix[right] - array_sorted_prefix[left - 1])
