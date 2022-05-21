#пункт а
ls = [34.50, 50.90, 46, 90.10, 91.08, 63.50, 34, 80, 77.50, 16]
ls_2 = []
for i in ls:
    num = '%.2f' % i
    num = num.replace('.', ' руб ')
    a = f'{num} коп'
    ls_2.append(a)
print(', '.join(ls_2))

#пункт b, c, d

print('Список первоначальный:', id(ls), ls)
ls.sort()
print('Cписок по возрастанию: ', id(ls), ls)
sorted_ls = sorted(ls, reverse=True)
print('Список по убыванию: ', id(sorted_ls), sorted_ls)
ls.sort()
print('Пятерка самых высоких цен: ', ls[5:])








