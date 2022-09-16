import math

a = int(input('Введите число а: '))

b = int(input('Введите число b: '))

number_sum = a + b
number_min = a - b
umn = a * b
cha = a / b
ost = a % b
log = math.log10(a)
step = a ** b

print('Сумма a и b =', number_sum)
print('Разность a и b =', number_min)
print('Произведение a и b =', umn)
print('Частное от делений a на b =', cha)
print('Остаток от деления a на b =', ost)
print('Десятичный логарифм от числа a =', log)
print('Результат возведения числа a в степень b =', step)
