from bisect import bisect_right

n = int(input())
array = list(map(int, input().split()))

array.sort()

q = int(input())
for _ in range(q):
    m = int(input())
    answer = bisect_right(array, m)

    print(answer)
