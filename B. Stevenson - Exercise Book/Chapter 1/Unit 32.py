number = int(input('Введите четырёхзначное число: '))

number = str(number)
number_1 = int(number[0])
number_2 = int(number[1])
number_3 = int(number[2])
number_4 = int(number[3])

number_sum = number_1 + number_2 + number_3 + number_4


print('Сумма равна:', number_sum)
