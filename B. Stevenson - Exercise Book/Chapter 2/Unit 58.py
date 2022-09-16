year = int(input('Введите год: '))

if year % 400 == 0:
    leap_year = 'високосный'
elif year % 100 == 0:
    leap_year = 'не високосный'
elif year % 4 == 0:
    leap_year = 'високосный'
else:
    leap_year = 'не високосный'

print('Введенный год -', leap_year)
