R = 8.314
Rat_kelv = 273.15
P = int(input('Введите давление в Па: '))
V = float(input('Введите объем в литрах: '))
T = float(input('Введите температуру в градусах Цельсия: '))

T_kelv = T + Rat_kelv

n = (P * V) / (R * T_kelv)

print('Количество вещества в молях:', round(n, 2))
