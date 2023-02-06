import datetime

def log_imp(sern):
    with open('log.txt', 'a', encoding='utf-8') as file:
        file.write(f'Запрос по фамилии {sern} осуществлен в {datetime.datetime.now()} \n')


def log_exp(result):
    with open('log.txt', 'a', encoding='utf-8') as file:
        file.write(f'Данные {result} были записаны в {datetime.datetime.now()} \n')
