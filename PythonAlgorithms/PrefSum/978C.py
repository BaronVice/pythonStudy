from bisect import bisect_left

n, m = map(int, input().split())

a = tuple(map(int, input().split()))
a_prefix = [0]
for i in range(n):
    a_prefix.append(a_prefix[i] + a[i])

b = tuple(map(int, input().split()))
for el in b:
    apartment = bisect_left(a_prefix, el)
    number = el - a_prefix[apartment-1]
    print(apartment, number)
