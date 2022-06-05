# Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово
# yield, например:


def odd_nums(number):
    for num in range(1, number + 1, 2):
        yield num


odd_to_15 = odd_nums(15)
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))

