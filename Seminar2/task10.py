# На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.

# 5 -> 1 0 1 1 0
# 2

n = int(input('Введите количество монет: '))
x = 0
y = 0

for i in range(n):
    side = int(input('Введите сторонy монеты (1 или 0): '))
    if side == 1:
        x += 1
    else:
        y += 1

if x < y:
    print(x)
else:
    print(y)