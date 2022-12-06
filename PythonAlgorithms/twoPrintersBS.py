
def number_of_sheets(t, x, y):
    return t//x + t//y


def find_time(n, x, y):
    l = 0
    r = min(x,y) * n
    mid = 0
    current_result = number_of_sheets(mid, x, y)

    while current_result < n:
        mid = (l + r) // 2
        current_result = number_of_sheets(mid, x, y)

        if current_result > n:
            r = mid
        else:
            l = mid + 1

    return mid


n, x, y = map(int, input().split())
n -= 1
print(find_time(n, x, y) + min(x,y))