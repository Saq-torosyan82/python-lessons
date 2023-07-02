# Заполните массив элементами арифметической
# прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для
# получения n-го члена прогрессии: a
# n
#  = a1
#  + (n-1) * d.
# Каждое число вводится с новой строки.

# Ввод: 7 2 5
# Вывод: 7 9 11 13 15

firstNum = int(input('Vvedite pervioe chislo: '))
diff = int(input('Vvedite raznost: '))
cnt = int(input('Vvedite kolichestvo chlenov: '))

print('Chleni progresii: ')
for i in range(cnt):
    print(firstNum + i * diff)
