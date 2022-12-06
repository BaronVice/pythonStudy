a, b = map(int, input().split())

mid = b
result = [mid]
while (mid % 2 == 0 or mid % 10 == 1) and a < mid:
    if not mid % 2:
        mid //= 2
        result.append(mid)
    else:
        mid //= 10
        result.append(mid)

if a == mid:
    print("YES")
    print(len(result))
    print(*result[::-1])
else:
    print("NO")
