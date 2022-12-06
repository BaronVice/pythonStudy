from time import time

# Или почему лучше использовать tuple, если не требуется менять элементы коллекции

n = 10000000
first_start = time()
a = tuple((t,) for t in range(n))
first_end = time()

second_start = time()
b = list([t] for t in range(n))
second_end = time()

print(first_end - first_start, second_end - second_start, sep = "\n")
