ls = list(range(1, 1000, 2))
ls_1 = []
for i in ls:
    j = i**3
    ls_1.append(j)
print(ls_1)

ls_2 = []
for j in ls_1:
    a = j % 10
    b = (j // 10) % 10
    c = ((j // 10) // 10) % 10
    d = ((j // 10) // 10) // 10
    summa = a + b + c + d
    if summa % 7 == 0:
        ls_2.append(j)
print(ls_2)

for j in ls_1:
    y = j + 17
    a1 = y % 10
    b1 = (y // 10) % 10
    c1 = ((y // 10) // 10) % 10
    d1 = ((y // 10) // 10) // 10
    summa = a1 + b1 + c1 + d1
    if summa % 7 == 0:
        print('сумма делится на 7 нацело :', summa)
