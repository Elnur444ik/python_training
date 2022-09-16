rating = float(input('Введите рейтинг сотрудника (0.0, 0.4, 0.6 и выше): '))

if rating == 0.0:
    level = 'низкий'
elif rating == 0.4:
    level = 'удовлетворительный'
elif rating >= 0.6:
    level = 'высокий'
else:
    level = 'error'

if level == 'error':
    print('Введено некорректное значение')
else:
    print('Ваш уровень:', level)
    prize = 2400 * rating
    print('Ваша надбавка составляет: $', round(prize, 2))
