weight = float(input('Введите свой вес в кг: '))
height = float(input('Введите свой рост в см: '))

BMI = (weight / height ** 2) * 10000
print('Индекс массы тела равен', round(BMI, 2))
