ls = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
ls_2 = []

for j in ls:
    if j.isdigit():
        ls_2.extend(['"', f'{int(j):02}', '"'])
    elif j[1:].isdigit():
        ls_2.extend(['"', f'{j[0]}{int(j):02}', '"'])
    else:
        ls_2.append(j)
print(ls_2)

ls_2 = ' '.join(ls_2)
print(ls_2)




