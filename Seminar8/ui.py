from actions import input_data, print_data, delete_data, update_data

def interface():
    print('Добрый день! Это бот-помощник.\n'
          'Что Вы хотите сделать? \n'
          '1 - Записать данные \n'
          '2 - Вывести данные\n'
          '3 - Удалить данные\n'
          '4 - Изменить данные\n')
    
    command = int(input('Ваш выбор: '))

    while command not in [1, 2, 3, 4]:
        command = int(input('Ошибка! Попробуйт ещё раз! Ваш выбор: '))

    match command:
        case 1:
            input_data()
        case 2:
            print_data()
        case 3:
            delete_data()
        case 4:
            update_data()
        