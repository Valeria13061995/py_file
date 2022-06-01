# Написать функцию currency_rates(), принимающую в качестве аргумента код валюты
# (например, USD, EUR, GBP, ...) и возвращающую курс этой валюты по отношению к рублю.
# Использовать библиотеку requests. В качестве API можно использовать
# http://www.cbr.ru/scripts/XML_daily.asp. Рекомендация: выполнить предварительно запрос к API
# в обычном браузере, посмотреть содержимое ответа. Можно ли, используя только методы класса
# str, решить поставленную задачу? Функция должна возвращать результат числового типа,
# например float. Подумайте: есть ли смысл для работы с денежными величинами использовать
# вместо float тип Decimal? Сильно ли усложняется код функции при этом? Если в качестве
# аргумента передали код валюты, которого нет в ответе, вернуть None. Можно ли сделать работу
# функции не зависящей от того, в каком регистре был передан аргумент? В качестве примера
# выведите курсы доллара и евро.
# from typing import Set

# *(вместо 2) Доработать функцию currency_rates(): теперь она должна возвращать кроме курса
# дату, которая передаётся в ответе сервера. Дата должна быть в виде объекта date. Подумайте,
# как извлечь дату из ответа, какой тип данных лучше использовать в ответе функции?


import requests
import xmltodict
import datetime


def currency_rates(current):
    global money
    page = requests.get('http://www.cbr.ru/scripts/XML_daily.asp').text
    site = xmltodict.parse(page)
    for j in site['ValCurs']['Valute']:
        if j['CharCode'] == current.upper():
            money = j['Value']
            print(f'{money}')

    time_money = site['ValCurs']['@Date']
    data_string = datetime.datetime.strptime(time_money, '%d.%m.%Y').date()
    print(f'{site},{data_string},{money}')
    print(type(data_string))

if __name__ == '__main__':
    currency_rates('eur')
