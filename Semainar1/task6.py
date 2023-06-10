# Вы пользуетесь общественным транспортом? Вероятно, вы
# расплачивались за проезд и получали билет с номером. Счастливым
# билетом называют такой билет с шестизначным номером, где сумма
# первых трех цифр равна сумме последних трех. Т.е. билет с номером
# 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
# программу, которая проверяет счастливость билета.

# *Пример:*

# 385916 -> yes
# 123456 -> no

n = int(input('Введите номер билета с шестизначным числом: '))

if n < 100000 or n > 999999:
    print('Неправыльное число')
else:
    leftNum = n // 1000
    print('leftNum = ',leftNum)
    leftSum = leftNum % 10
    leftNum = leftNum // 10
    leftSum += leftNum % 10
    leftNum = leftNum // 10
    leftSum += leftNum
    print('leftSum = ',leftSum)

    rightNum = n % 1000
    print('rightNum = ',rightNum)
    rightSum = rightNum % 10
    rightNum = rightNum // 10
    rightSum += rightNum % 10
    rightNum = rightNum // 10
    rightSum += rightNum
    print('rightSum = ',rightSum)

    if leftSum == rightSum:
        print(n, ' - YES')
    else:    
        print(n, ' - NO')
