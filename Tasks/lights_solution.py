n, l = map(int, input().split())
lights_coordinates = list(set(map(int, input().split())))
lights_coordinates.sort()

first_case = lights_coordinates[0]
second_case = l - lights_coordinates[-1]

third_case = 0
for i in range(len(lights_coordinates)-1):
    radius = (lights_coordinates[i + 1] - lights_coordinates[i]) / 2
    if third_case < radius:
        third_case = radius
print(max(first_case, second_case, third_case))