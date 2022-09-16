import math

r = float(input('Введите радиус: '))

area = math.pi * r**2

volume = 4/3 * math.pi * r**3

print('Площадь круга:', round(area, 2))
print('Площадь шара:', round(volume, 2))
