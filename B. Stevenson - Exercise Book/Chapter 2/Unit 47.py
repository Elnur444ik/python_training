month = input('Введите месяц: ')
day = int(input('Введите номер дня: '))
season = ' '
if month in ['Январь', 'Февраль']:
    season = 'Зима'
elif month == 'Декабрь':
    if day > 21:
        season = 'Зима'
    else:
        season = 'Осень'
elif month == 'Март':
    if day > 20:
        season = 'Весна'
    else:
        season = 'Зима'
elif month in ['Апрель', 'Май']:
    season = 'Весна'
elif month == 'Июнь':
    if day > 21:
        season = 'Лето'
    else:
        season = 'Весна'
elif month in ['Июль', 'Август']:
    season = 'Лето'
elif month == 'Сентябрь':
    if day > 22:
        season = 'Осень'
    else:
        season = 'Лето'
elif month in ['Октябрь', 'Ноябрь']:
    season = 'Осень'

print('Сезон:', season)
