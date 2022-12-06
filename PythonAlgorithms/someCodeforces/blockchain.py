n, c = map(int, input().split())


def convert_to_sec(inp):
    return int(inp[0:2]) * 3600 + int(inp[3:5]) * 60 + int(inp[6:])


arr = []
for _ in range(n):
    start, stop, reward = input().split()
    start_to_seconds = convert_to_sec(start)
    end_to_seconds = convert_to_sec(stop)
    arr.append((start_to_seconds, end_to_seconds, int(reward)))

arr.sort(key=lambda el: el[0])

result = 0
for el in arr:
    print(el)
#for i in range(n):
#    current_result = 0
#    expenses = 0


