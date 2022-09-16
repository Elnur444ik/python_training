import math

r = float(input('Введите радиус цилиндра '))
h = float(input('Введите высоту цилиндра '))

volume = math.pi * h * r ** 2

print('Объем цилиндра равен', round(volume, 1))
