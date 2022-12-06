n, s = map(int, input().split())
cost = list(map(int, input().split()))

right = n + 1
left = 0

k = 0
expenses = 0

while left + 1 < right:
    sorted_costs_including_k = []

    mid = (left + right) // 2
    for i in range(n):
        sorted_costs_including_k.append(cost[i] + (i + 1) * mid)

    sorted_costs_including_k.sort()
    current_case_cost = 0
    for i in range(mid):
        current_case_cost += sorted_costs_including_k[i]

    if current_case_cost <= s:
        k = mid
        expenses = current_case_cost
        left = mid
    else:
        right = mid

print(k, expenses)
