def inp_mod():
    mod = input('Введите режим работы (импорт - 1 или экспорт - 2): ')
    return mod


def inp_import():
    surname = input('Введите фамилию для поиска: ')
    return surname    

def view_import (result):
    print(*result, sep='\n')

def inp_export():
    surname = input('Введите фамилию: ')
    name = input('Введите имя: ')
    sec_name = input('Введите отчество: ')
    phone = input('Введите телефон: ')
    comment = input('Введите тип телефона (домашний, рабочий и т.д.): ')
    return '\n', surname, name, sec_name, phone, comment

def view_import_no ():
    print(f"Данные не найдены")