from data_generator import input_user_data

def input_data():
    name, surname, phone, adress = input_user_data()
    variant = int(input(f'\nВ каком виде записать данные?\n'
                    f'1 Вариант: \n'
                    f'{name}\n'
                    f'{surname}\n'
                    f'{phone}\n'
                    f'{adress}\n\n'
                    f'2 Вариант: \n'
                    f'{name};{surname};{phone};{adress}\n\n'
                    f'Ваш выбор:'))
    
    match variant:
        case 1:
            from writer import v1 as writeFile            
        case 2:
            from writer import v2 as writeFile
        case _:
            return print('Нет такого файла')
    
    writeFile(name, surname, phone, adress)

    print(f'Dannie dobavleni v {variant}')

def print_data():
    variant = int(input(f'\nИз какого варианта показать данные? '))

    match variant:
        case 1:
            from reader import v1 as readFile
        case 2:
            from reader import v2 as readFile
        case _:
            return print('Нет такого файла')

    readFile()
        

def delete_data():
    variant = int(input(f'\nИз какого файла удалить данные ? '))

    match variant:
        case 1:
            from data_delete import v1 as deleteData
        case 2:
            from data_delete import v2 as deleteData
        case _:
            return print('Нет такого файла')

    dataNum = int(input(f'\nКакую запись удалить ? '))

    deleteData(dataNum)

def update_data():
    variant = int(input(f'\nВ каком файле изменить данные ? '))

    match variant:
        case 1:
            from update_data import v1 as updateData
        case 2:
            from update_data import v2 as updateData
        case _:
            return print('Нет такого файла')

    dataNum = int(input(f'\nКакую запись изменить ? '))

    updateData(dataNum)
    
    