from sys import setrecursionlimit
setrecursionlimit(12)


# Вы понимаете рекурсию
def recursion(i):
    n = input("Вы понимаете рекурсию?: ")
    if n == "Да":
        print(f"Вы поняли рекурсию за {i} итераций")
        return
    else:
        recursion(i)


try:
    recursion(0)
except RecursionError:
    print("Увы, превышена максимальная глубина рекурсии")
