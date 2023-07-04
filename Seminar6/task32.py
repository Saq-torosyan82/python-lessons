# Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

# индексы: 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19
# Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# 7 10
# Вывод: [1, 9, 13, 14, 19]

import random

# myList = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
myList = [random.randint(-50, 50) for i in range(int(input('n = ')))]
min = int(input('Vvedite minimum chislo: '))
max = int(input('VVedite maximum chislo: '))

indexes = list()

for i in range(len(myList)):
    if min <= myList[i] <= max:
        indexes.append(i)

print(indexes) 
