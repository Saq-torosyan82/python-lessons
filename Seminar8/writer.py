def v1(name, surname, phone, adress):
    from files import file_1

    with open(file_1(), 'a', encoding='utf-8') as file:
        file.write(f'{name}\n'
                   f'{surname}\n'
                   f'{phone}\n'
                   f'{adress}\n\n')

def v2(name, surname, phone, adress):
    from files import file_2

    with open(file_2(), 'a', encoding='utf-8') as file:
        file.write(f'{name};{surname};{phone};{adress}\n\n')
