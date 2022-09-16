side = int(input('Введите количество сторон фигуры от 3 до 10 включительно: '))
figure = ' '
if side == 3:
    figure = 'треугольник'
elif side == 4:
    figure = 'четырехугольник'
elif side == 5:
    figure = 'пятиугольник'
elif side == 6:
    figure = 'шестиугольник'
elif side == 7:
    figure = 'семиугольник'
elif side == 8:
    figure = 'восьмиугольник'
elif side == 9:
    figure = 'девятиугольник'
elif side == 10:
    figure = 'десятиугольник'

if figure == ' ':
    print('Введенное значение выходит за границы диапазона')
else:
    print('Эта фигура:', figure)
