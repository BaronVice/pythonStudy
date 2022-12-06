# from math import ceil
#
# s, p = map(int, input().split())
# for i in range(1, ceil(p**0.5)+1):
#     if p % i == 0:
#         if i + p//i == s:
#             print(i, p//i)
#             break


n = int(input())
for _ in range(n):
    s = input()
    print("No") if int(s, 2) % 7 else print("Yes")