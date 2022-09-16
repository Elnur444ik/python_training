import math

t1 = float(input('Введите координаты широты первой точки в градусах: '))
g1 = float(input('Введите координаты долготы первой точки в градусах: '))

t2 = float(input('Введите координаты широты второй точки в градусах: '))
g2 = float(input('Введите координаты долготы второй точки в градусах: '))

t1_rad = math.radians(t1)
g1_rad = math.radians(g1)
t2_rad = math.radians(t2)
g2_rad = math.radians(g2)

distance = 6371.01 * math.acos(math.sin(t1_rad) *
                               math.sin(t2_rad) + math.cos(t1_rad) * math.cos(t2_rad) * math.cos(g1_rad - g2_rad))

print('Расстояние от первой точки до второй равно ', round(distance, 2), 'км')
