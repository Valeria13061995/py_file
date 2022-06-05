# *(вместо 1) Решить задачу генерации нечётных чисел от 1 до n (включительно), не используя
# ключевое слово yield

num = int(input('Введите любое число: '))
odd_nums = (i for i in range(1, num + 1, 2))

print(next(odd_nums))
print(next(odd_nums))
print(next(odd_nums))
print(next(odd_nums))