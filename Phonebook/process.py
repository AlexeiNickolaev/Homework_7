def search(sn):
    res_list = []
    path = 'Phonebook\data.txt'
    with open(path, 'r', encoding = 'utf-8') as file:
        while True:
            my_book = file.readline()
            if not my_book:
                if not file.readline():
                    break
            if my_book.rstrip() == sn:
                res_list.append(sn)
                for i in range(1, 5):
                    res_list.append(file.readline().rstrip())
                res_list.append('')
    if len(res_list) > 0:
        return res_list
    return 'Таких людей нет'