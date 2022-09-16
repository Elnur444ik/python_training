number = int(input('Введите целое число (0 для выхода): '))
mean = 0
step = 0
total = 0
while number != 0:
    step += 1
    total += number
    mean = total / step
    print('Среднее арифмитическое:', mean)
    number = int(input('Введите целое число (0 для выхода): '))
if number == 0 and total == 0:
    print('Ошибка. Первое значение равно 0.')
else:
    print('Среднее арифмитическое:', mean)

