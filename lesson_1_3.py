import pymorphy2

morph = pymorphy2.MorphAnalyzer()
word = morph.parse('процент')[0]
result = word.make_agree_with_number(2).word
print(result)

# как записать в столбец через input не совсем понятно
# прошу объяснить, как сделать задачу правильно, именно через данный способ словаря
# спасибо
# второй вариант

for i in range (1, 100):
  if i == 1:
    print(i, 'поцент')
  elif 1 < i <= 4:
    print(i, 'процента')
  elif 4 < i <= 20:
    print(i, 'процентов')
  elif 20 < i and i % 10 == 1:
    print(i, 'процент')
  elif 2 <= i % 4 == 4:
    print(i, 'провента')
  else:
    print(i, 'процентов')
