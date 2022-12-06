

def count_expenses(picked_k):
    current_prices = [a[i] + (i+1) * picked_k for i in range(n)]
    current_prices.sort()

    result = 0
    for i in range(picked_k):
        result += current_prices[i]
    return result


n, S = map(int, input().split())
a = tuple(map(int, input().split()))

left = 0
right = n+1

k = 0
T = 0

while left + 1 < right:

    mid = (left + right) // 2

    current_expenses = count_expenses(mid)
    if current_expenses <= S:
        k = mid
        T = current_expenses
        left = mid
    else:
        right = mid

print(k, T)
