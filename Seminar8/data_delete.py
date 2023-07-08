def v1(dataNum):
    from files import file_1

    with open(file_1(), 'r+', encoding='utf-8') as file:
        data = file.readlines()
        start = (dataNum - 1) * 5
        end = start + 4
        dataToDelete = data[start : end]

        if len(dataToDelete) == 0:
            print('Нет такой записи')
        else:
            if dataNum == 1:
                newData = data[end + 1:]
            else:
                newData = data[:start] + data[end + 1:]

            file.seek(0)
            file.write(''.join(newData))
            file.truncate()

def v2(dataNum):
    from files import file_2

    with open(file_2(), 'r+', encoding='utf-8') as file:
        data = file.readlines()
        print(data)
        deleteIndex = (dataNum - 1) * 2

        if deleteIndex >= len(data):
            print('Нет такой записи')
        else:
            dataToDelete = data[deleteIndex]
            print(dataToDelete)
            if dataNum == 1:
                newData = data[deleteIndex + 2:]
            else:
                newData = data[:deleteIndex] + data[deleteIndex + 2:]

            file.seek(0)
            print(newData)
            file.write(''.join(newData))
            file.truncate()