K_CONST = 273.15
F_CONST_1 = 1.8
F_CONST_2 = 32

C = float(input('Введите температуру в градусах Цельсия: '))

K = C + K_CONST

F = C * F_CONST_1 + F_CONST_2

print('В Кельвинах равно: ', round(K, 2))

print('В Фаренгейтах равно:', round(F, 2))
