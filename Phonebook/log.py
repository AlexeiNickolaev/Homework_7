import datetime

def log_imp(sern):
    path = 'Phonebook\log.txt'
    with open(path, 'a', encoding='utf-8') as file:
        file.write(f'Запрос по фамилии {sern} осуществлен в {datetime.datetime.now()} \n')


def log_exp(result):
    path = 'Phonebook\log.txt'
    with open(path, 'a', encoding='utf-8') as file:
        file.write(f'Данные {result} были записаны в {datetime.datetime.now()} \n')
