def inp_mod():
    mod = input('Введите режим работы (импорт или экспорт): ')
    return mod


def inp_import():
    surname = input('Введите фамилию для поиска: ')
    return surname    

def view_import (result):
    print(*result, sep='\n')

def view_import_no ():
    print(f"Данные не найдены")