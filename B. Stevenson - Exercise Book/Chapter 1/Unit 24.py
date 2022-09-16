days = int(input('Введите количество дней: '))
hours = int(input('Введите количество часов: '))
minutes = int(input('Введите количество минут: '))
seconds = int(input('Введите количество секунд: '))

days_to_sec = days * 24 * 60 * 60
hours_to_sec = hours * 60 * 60
minutes_to_sec = minutes * 60

total_seconds = days_to_sec + hours_to_sec + minutes_to_sec + seconds

print('В ведденом отрезке', total_seconds, 'секунд')
