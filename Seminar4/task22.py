# Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.

# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12

n = int(input('Enter the number of the first list: '))
m = int(input('Enter the number of the second list: '))

list_1 = list()
list_2 = list()

for i in range(n):
    num = int(input('Enter an integer number for the first list: '))
    list_1.append(num)

print(list_1)

for i in range(m):
    num = int(input('Enter an integer number for the second list: '))
    list_2.append(num)

print(list_2)

res_set = set()


if n < m:
    for i in list_1:
        if i in list_2:
            res_set.add(i)
else:
    for i in list_2:
        if i in list_1:
            res_set.add(i)

print(sorted(res_set))