# Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца.
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны.
# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).
# Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.

# *Пример:*

# **Ввод:** `print_operation_table(lambda x, y: x * y) ` 
# **Вывод:**
# 1 2 3 4 5 6

# 2 4 6 8 10 12
# 3 6 9 12 15 18
# 4 8 12 16 20 24
# 5 10 15 20 25 30
# 6 12 18 24 30 36

num_rows = int(input('Enter num rows (> 0): '))
num_columns = int(input('Enter num columns (> 0): '))

def print_operation_table(operation, num_row = 6, num_column = 6):
    return operation(num_row, num_column)

rows = list()
def drawTable(num_rows, num_columns):
    for r in range(1, num_rows + 1):
        row = list()
        for c in range(1, num_columns + 1):
            row.append(str(print_operation_table(lambda x, y: x * y, r, c)))
        rows.append(' '.join(row))

    print('\n'.join(rows))

drawTable(num_rows, num_columns)