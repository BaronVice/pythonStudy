

n = int(input())

result = 0
while len(str(n)) > 1:
    current_len = len(str(n))
    next_number = int('9' * (current_len-1))
    while next_number % current_len != n % current_len:
        next_number -= 1
    result += (n - next_number) // current_len
    n = next_number

result += n
print(result)
