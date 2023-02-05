import datetime

def log_imp(surname):
    with open('log.txt', 'a', encoding='utf-8') as file:
        file.write(f'Запрос по фамилии {surname} осуществлен в {datetime.datetime.now()} \n')


def log_exp(surname, name, sec_name, phone, comment):
    with open('log.txt', 'a', encoding='utf-8') as file:
        file.write(f'Данные {surname, name, sec_name, phone, comment} были записаны в {datetime.datetime.now()} \n')
