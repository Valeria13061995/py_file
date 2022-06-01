# 2. * (вместо задачи 1) Доработать предыдущую функцию в num_translate_adv():
# реализовать корректную работу с числительными, начинающимися с заглавной буквы —
# результат тоже должен быть с заглавной. Например:
# >>> num_translate_adv("One")
# "Один"
# >>> num_translate_adv("two")
# "два"

numbers = {'one': 'один',
           'two': 'два',
           'three': 'три',
           'four': 'четыре',
           'five': 'пять',
           'six': 'шесть',
           'seven': 'семь',
           'eight': 'восемь',
           'nine': 'девять',
           'ten': 'десять'
}

def num_translate_adv(num):
    if num.istitle() == True:
        num = num.lower()
        return (numbers.get(num).capitalize())
    else:
        return (numbers.get(num))
a = num_translate_adv('one')
print(a)