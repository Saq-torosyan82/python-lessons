from data_generator import input_user_data

def v1(dataNum):
    from files import file_1

    with open(file_1(), 'r+', encoding='utf-8') as file:
        data = file.readlines()
        start = (dataNum - 1) * 5
        end = start + 3

        if len(data[start : end]) == 0:
            print('Нет такой записи')
        else:
            name, surname, phone, adress = input_user_data()

            data[start] = name + '\n'
            data[start + 1] = surname + '\n'
            data[start + 2] = phone+ '\n'
            data[start + 3] = adress + '\n'

            file.seek(0)
            file.write(''.join(data))
            file.truncate()

def v2(dataNum):
    from files import file_2

    with open(file_2(), 'r+', encoding='utf-8') as file:
        data = file.readlines()
        print(data)
        updateIndex = (dataNum - 1) * 2

        if updateIndex >= len(data):
            print('Нет такой записи')
        else:
            name, surname, phone, adress = input_user_data()
            data[updateIndex] = f'{name};{surname};{phone};{adress}\n'

            file.seek(0)
            file.write(''.join(data))
            file.truncate()