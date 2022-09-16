n = int(input('Введите целое число: '))
factor = 2
if n >= 2:
    while factor <= n:
        if n % factor == 0:
            n = n // factor
            print(factor)
        else:
            factor += 1
    print('Расчет окончен')
else:
    print('Введено некорректное значение')

