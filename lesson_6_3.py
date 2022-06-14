#  Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби.
# Известно, что при хранении данных используется принцип: одна строка — один пользователь,
# разделитель между значениями — запятая. Написать код, загружающий данные из обоих файлов
# и формирующий из них словарь: ключи — ФИО, значения — данные о хобби. Сохранить словарь
# в файл. Проверить сохранённые данные. Если в файле, хранящем данные о хобби, меньше
# записей, чем в файле с ФИО, задаём в словаре значение None. Если наоборот — выходим из
# скрипта с кодом «1». При решении задачи считать, что объём данных в файлах во много раз
# меньше объема ОЗУ.
# Фрагмент файла с данными о пользователях (users.csv):
# Иванов,Иван,Иванович
# Петров,Петр,Петрович
# Фрагмент файла с данными о хобби (hobby.csv):
# скалолазание,охота
from itertools import zip_longest
import json


user = open('user.csv.txt', encoding='UTF-8')
hobby = open('hobby.csv.txt', encoding='UTF-8')

key_user = list(k.strip() for k in user)
val_hobby = list(v.strip() for v in hobby)

if len(val_hobby) > len(key_user):
    my_dict = {key: val for key, val in zip_longest(key_user, val_hobby)}
    print(my_dict)
    with open('file_3.txt', 'w', encoding='utf-8') as f:
        json.dump(my_dict, f, ensure_ascii=False)
else:
    exit(1)




















# long_name = str(sum(1 for lines in name))
# long_hobby = str(sum(1 for lines in hobby))
# for lines in name, hobby:
#      if long_name <= long_hobby:
#          exit(1)
#
#      name.seek(0)
#      hobby.seek(0)
#     # rez = ((i, j) for i, j in zip_longest(name, hobby, fillvalue=None))
#     for long_name, long_hobby in zip_longest(name, hobby):
#         user_dict[long_name.strip()] = long_name_hobby.strip() if
#         print(user_dict)
#
#
#
#
#     # print(next(rez))
#     # print(next(rez))
#     # print(next(rez))
#     # print(next(rez))
#     # print(next(rez))
#     # print(next(rez))
#



