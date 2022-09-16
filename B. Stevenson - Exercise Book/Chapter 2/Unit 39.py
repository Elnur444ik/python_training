month = input('Введите месяц: ')
days = 0
day_30 = ['Апрель', 'Июнь', 'Сентябрь', 'Ноябрь']
day_31 = ['Январь', 'Март', 'Май', 'Июль', 'Август', 'Октябрь', 'Декабрь']
day_february = ['Февраль']
if month in day_30:
    days = 30
elif month in day_31:
    days = 31
elif month in day_february:
    days = 28/29

if days == 0:
    print('Месяц введен некорректно')
else:
    print('В введенном месяце:', days, 'дней.')
