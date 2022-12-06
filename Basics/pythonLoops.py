

a = 1
# Пример цикла while: проходим итерации до тех пор, пока выполняется условие
while a <= 10:
    if a % 2 == 0:
        print(a)
    a += 1

numbers = [1, 2, 3, 4, 5, 6]
# Цикл можно сделать проходя по элементам коллекции
for number in numbers:
    print(number)
else:
    print("Цикл успешно завершился", f"Последний элемент массива: {number}", sep="\n")


# range тоже коллекция - формирует список целых чисел в диапазоне от [start, end)
# Если укажем только одно число, то по умолчанию start будет взят за 0

# Цикл в цикле - это вложенный цикл
for i in range(4):
    for j in range(4):
        print(i, j, sep='\t')

for i in range(1, 11):
    # Если цикл наткнулся на continue, то он завершит текущую итерацию и перейдет на новую
    if i == 2:
        continue
    # Если цикл наткнулся на break, то цикл завершится (полностью выйдем из него)
    if i == 7:
        break
    print(i)

# Лишний раз continue и break лучше не использовать, но если очень надо, то пишите
