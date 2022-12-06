

def bin_find(to_find, array):
    l, r = 0, len(array)
    while l + 1 < r:
        m = (l + r) // 2
        if array[m] > to_find:
            r = m
        else:
            l = m
    return l < len(array) and array[l] == to_find


a = [1, 2, 6, 8, 9, 11]
for i in range(10):
    print(f"{i} in a: {bin_find(i, a)}")