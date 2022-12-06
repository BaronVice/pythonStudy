
n = int(input())
array = tuple(map(int, input().split()))

min_el = min(array)

if array.count(min_el) == 1:
    print(n * min_el + n-1)

else:
    first_occurence = array.index(min_el)
    right_pointer = first_occurence

    max_len = 0

    for i in range(first_occurence + 1, n):
        if min_el == array[i]:
            if i - right_pointer > max_len:
                max_len = i - right_pointer
            right_pointer = i

    first_last_case_len = first_occurence + n - right_pointer
    if first_last_case_len < max_len:
        print(n * min_el + max_len - 1)
    else:
        print(n * min_el + first_last_case_len - 1)