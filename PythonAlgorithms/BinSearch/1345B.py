# Вместо бин поиска
from bisect import bisect_right


def pyramids(cards):
    # Изначально ничего не строим
    result = 0
    # Пирамида получится, если есть хотя бы две карточки
    while cards >= 2:
        # Находим позицию
        pos = bisect_right(cards_needed, cards)
        result += 1
        cards -= cards_needed[pos-1]
    return result


# Это максимум карточек
maxx = 1000000000
# Изначально на первую пирамидку нужно две карточки
cards_needed = [2]
# Для следующей на 5 больше
to_add = 5
i = 0

while cards_needed[i] < maxx:
    # Считаем расход карточек на i-высоту пирамиды (к предыдущему значению прибавляем разницу)
    cards_needed.append(cards_needed[i] + to_add)
    i += 1
    # И для последующих разница будет увеличиваться на 3
    to_add += 3

# С кортежем будет быстрее
cards_needed = tuple(cards_needed)

t = int(input())
for _ in range(t):
    # Для каждого запроса дадим ответ
    n = int(input())
    print(pyramids(n))
