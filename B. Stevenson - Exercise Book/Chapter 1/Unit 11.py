MPG = float(input('Введите потребление топлива в милях на галлон: '))

LPK = 378.5 / (MPG * 1.609)

print('Потребление топлива в канадских единицах будет равно ', round(LPK, 2), 'л/100 км')
