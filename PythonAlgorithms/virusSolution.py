t = int(input())

for _ in range(t):
    total, infected = map(int, input().split())
    infected_coordinates = sorted(list(map(int, input().split())))

    healthy_lines = [infected_coordinates[0] - 1 + total - infected_coordinates[-1]]
    for i in range(infected-1):
        healthy_lines.append(infected_coordinates[i+1] - infected_coordinates[i] - 1)
    healthy_lines.sort()

    saved = 0
    while healthy_lines[-1] > 0:
        if healthy_lines[-1] <= 2:
            saved += 1
        else:
            saved += healthy_lines.pop() - 1
        healthy_lines = [el-2 for el in healthy_lines]
    print(total-saved)
