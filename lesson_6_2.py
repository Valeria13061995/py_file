# *(вместо 1) Найти IP адрес спамера и количество отправленных им запросов по данным файла
# логов из предыдущего задания.

from collections import Counter
with open('nginx_logs.txt') as f:
    my_list = []
    spam = {}
    for i in f:
        scr = i.split()
        my_list.append((scr[0], scr[5].replace('"', ''), scr[6]))
        spam.setdefault(scr[0], 0)
        spam[scr[0]] += 1
spam = sorted(Counter(spam).items(), key=lambda v: v[1], reverse=True)
print(spam[:3])




