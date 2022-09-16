day = input('Введите дату: ')
holiday = ' '
new_year = '1 января'
canada_day = '1 июля'
christmas = '25 декабря'
if day == new_year:
    holiday = 'Новый год'
elif day == canada_day:
    holiday = 'День Канады'
elif day == christmas:
    holiday = 'Рождество'
if holiday == ' ':
    print('В введенную дату нет праздников')
else:
    print('Праздник в этот день:', holiday)
