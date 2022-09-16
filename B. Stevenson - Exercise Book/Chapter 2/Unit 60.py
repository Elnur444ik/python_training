year = int(input('Введите год: '))

from math import floor

day_of_the_week = (year + floor((year - 1) / 4) - floor((year - 1) / 100) + floor((year - 1) / 400)) % 7
day = ' '
if day_of_the_week == 0:
    day = 'воскресенье'
elif day_of_the_week == 1:
    day = 'понедельник'
elif day_of_the_week == 2:
    day = 'вторник'
elif day_of_the_week == 3:
    day = 'среда'
elif day_of_the_week == 4:
    day = 'четверг'
elif day_of_the_week == 5:
    day = 'пятница'
elif day_of_the_week == 6:
    day = 'суббота'

print('В этом году 1 января - ', day)


