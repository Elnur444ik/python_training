decimal_number = int(input('Введите положительное десятичное число: '))
result = ''

if decimal_number > 0:
    while decimal_number != 0:
        r = decimal_number % 2
        result += str(r)
        decimal_number = decimal_number // 2
elif decimal_number == 0:
    result = '0'

result = result[::-1]

if result:
    print('Двоичное представление введеного числа равно:', result)
else:
    print('Введено некорректное значение')