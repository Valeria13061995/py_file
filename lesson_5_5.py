# Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать из этих элементов список с сохранением порядка их следования в исходном
# списке, например:
# src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# result = [23, 1, 3, 10, 4, 11]



from collections import Counter
# словарь, который позволяет считать количество неизменяемых объектов
mylist = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_list_1 = []
[new_list_1.append(i) for i in mylist if i not in new_list_1]
new_mylist_2 = []
[new_mylist_2.append(k) for k, v in Counter(mylist).items() if v > 1]
new_list_3 = [i for i in new_list_1 if i not in new_mylist_2]
print(new_list_3)



