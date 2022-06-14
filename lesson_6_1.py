# Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов
# web-сервера nginx_logs.txt
# (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs)
# — получить список кортежей вида: (<remote_addr>, <request_type>,
# <requested_resource>). Например:
# [
# ...
# ('141.138.90.60', 'GET', '/downloads/product_2'),
# ('141.138.90.60', 'GET', '/downloads/product_2'),
# ('173.255.199.22', 'GET', '/downloads/product_2'),
# f = open('nginx_logs.txt')
with open('nginx_logs.txt') as f:
     for i in f:
         my_list = []
         scr = i.split()
         my_list.append((scr[0], scr[5].replace('"', ''), scr[6]))
         print(my_list[0])

