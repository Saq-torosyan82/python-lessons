def v1():
    from files import file_1

    with open(file_1(), 'r', encoding='utf-8') as file:
        data = file.readlines()
        data_list = list()
        j = 0

        for i in range(len(data)):
            if data[i] == '\n':
                data_list.append(''.join(data[j:i]))
                j = i

        print(''.join(data_list))

def v2():
    from files import file_2

    with open(file_2(), 'r', encoding='utf-8') as file:
        data_list = list(file.readlines())
        print(''.join(data_list))