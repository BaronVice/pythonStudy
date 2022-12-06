def count_lines(picked_value, k):
    current_result = picked_value
    power_of_k = k
    while picked_value // power_of_k != 0:
        current_result += picked_value // power_of_k
        power_of_k *= k
    return current_result


n, k = map(int, input().split())

left = 0
right = n

while left + 1 < right:
    mid = (left + right) // 2
    if count_lines(mid, k) >= n:
        right = mid
    else:
        left = mid

print(right)
