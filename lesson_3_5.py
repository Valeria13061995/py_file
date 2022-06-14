# 5. Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов, взятых
# из трёх списков (по одному из каждого):
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
#         Например:
# >>> get_jokes(2)
# ["лес завтра зеленый", "город вчера веселый"]
# Документировать код функции.
# Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы
# слов в шутках (когда каждое слово можно использовать только в одной шутке)? Сможете ли вы сделать аргументы именованными?

import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

def get_jokes(number,replace=True ):
    """ returns the number of elements whether or not to repeat these elements, number: number of elements,
replace: true, false """

    my_list = []

    if not replace:
        if number > min((len(nouns)), (len(adverbs)), (len(adjectives))):
            return 'No'

        else:
            random.shuffle(nouns)
            random.shuffle(adverbs)
            random.shuffle(adjectives)
            for num in range(number):
                my_list.append(f'{nouns[num]} {adverbs[num]} {adjectives[num]}')
            return my_list

    else:
        for number in range(number):
            one_nouns = random.choice(nouns)
            one_adverbs = random.choice(adverbs)
            one_adjectives = random.choice(adjectives)
            my_list.append(f'{one_nouns}, {one_adverbs}, {one_adjectives}')
    return my_list

print(get_jokes(1, False))
print(get_jokes(2, False))
print(get_jokes(3, False))
print(get_jokes(4, False))




