day = int(input('Введите номер дня рождения: '))
month = input('Введите месяц рождения: ')
zodiac = ' '

if month == 'Январь':
    if day <= 19:
        zodiac = 'Козерог'
    else:
        zodiac = 'Водолей'
elif month == 'Февраль':
    if day <= 18:
        zodiac = 'Водолей'
    else:
        zodiac = 'Рыбы'
elif month == 'Март':
    if day <= 20:
        zodiac = 'Рыбы'
    else:
        zodiac = 'Овен'
elif month == 'Апрель':
    if day <= 19:
        zodiac = 'Овен'
    else:
        zodiac = 'Телец'
elif month == 'Май':
    if day <= 20:
        zodiac = 'Телец'
    else:
        zodiac = 'Близнецы'
elif month == 'Июнь':
    if day <= 20:
        zodiac = 'Близнецы'
    else:
        zodiac = 'Рак'
elif month == 'Июль':
    if day <= 22:
        zodiac = 'Рак'
    else:
        zodiac = 'Лев'
elif month == 'Август':
    if day <= 22:
        zodiac = 'Лев'
    else:
        zodiac = 'Дева'
elif month == 'Сентябрь':
    if day <= 22:
        zodiac = 'Дева'
    else:
        zodiac = 'Весы'
elif month == 'Октябрь':
    if day <= 22:
        zodiac = 'Весы'
    else:
        zodiac = 'Скорпион'
elif month == 'Ноябрь':
    if day <= 21:
        zodiac = 'Скорпион'
    else:
        zodiac = 'Стрелец'
elif month == 'Декабрь':
    if day <= 21:
        zodiac = 'Стрелец'
    else:
        zodiac = 'Козерог'

print('Ваш знак зодиака:', zodiac)


