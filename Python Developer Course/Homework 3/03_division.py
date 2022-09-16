# -*- coding: utf-8 -*-

# (цикл while)

# даны целые положительные числа a и b (a > b)
# Определить результат целочисленного деления a на b, с помощью цикла while,
# __НЕ__ используя стандартную операцию целочисленного деления (// и %)
# Формат вывода:
#   Целочисленное деление ХХХ на YYY дает ZZZ

#a, b = 179, 37
a, b = 200, 100
prom = b
step = 0
while a >= prom:
    step += 1
    prom = b * step
else:
    step -= 1
    print('Целочисленное деление', a, 'на', b, 'дает', step)
