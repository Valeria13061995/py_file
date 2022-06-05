# Представлен список чисел. Необходимо вывести те его элементы, значения которых больше
# предыдущего, например:
# src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# result = [12, 44, 4, 10, 78, 123]
# Подсказка: использовать возможности python, изученные на уроке. Подумайте, как можно
# сделать оптимизацию кода по памяти, по скорости.

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
my_list = [number for i, number in enumerate(src) if number > src[i - 1] and i != 0]
print(my_list)