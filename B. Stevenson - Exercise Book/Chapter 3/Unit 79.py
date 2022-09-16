number_1 = int(input('Введите первое число: '))
number_2 = int(input('Введите второе число: '))
d = min(number_1, number_2)

while (number_1 % d) != 0 or (number_2 % d) != 0:
    d -= 1

print('Наибольший общий делитель:', d)