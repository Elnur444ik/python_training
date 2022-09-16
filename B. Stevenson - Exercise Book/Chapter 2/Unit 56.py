frequence = int(input('Введите частоту: '))

if frequence < 3 * 10 ** 9:
    category = 'радиоволна'
elif 3 * 10 ** 9 <= frequence < 3 * 10 ** 12:
    category = 'микроволна'
elif 3 * 10 ** 12 <= frequence < 4.3 * 10 ** 14:
    category = 'инфракрасное излучение'
elif 4.3 * 10 ** 14 <= frequence < 7.5 * 10 ** 14:
    category = 'видимое излучение'
elif 7.5 * 10 ** 14 <= frequence < 3 * 10 ** 17:
    category = 'ультрафиолетовое излучение'
elif 3 * 10 ** 17 <= frequence < 3 * 10 ** 19:
    category = 'рентгеновское излучение'
elif frequence >= 3 * 10 ** 19:
    category = 'гамма-излучение'

print('Категория введенной частоты -', category)