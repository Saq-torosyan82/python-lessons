# Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.

# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

def calculateDegree(number, degree):
    if degree == 0:
        return 1

    return calculateDegree(number, degree - 1) * number

num = int(input('vvedite chislo: '))
deg = int(input('vvedite stepen: '))

print('Stepen',deg,'chisla',num,'ravno', calculateDegree(num, deg))