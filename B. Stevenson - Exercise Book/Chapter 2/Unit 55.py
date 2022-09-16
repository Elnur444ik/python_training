lenght = float(input('Введите длину волны в нм: '))

if 380 <= lenght < 450:
    color = 'фиолетовый'
elif 450 <= lenght < 495:
    color = 'синий'
elif 495 <= lenght < 570:
    color = 'зеленый'
elif 570 <= lenght < 590:
    color = 'желтый'
elif 590 <= lenght < 620:
    color = 'оранжевый'
elif 620 <= lenght <= 750:
    color = 'красный'
else:
    color = 'error'

if color == 'error':
    print('Введенное значение длины волны находится за пределами видимой части спектра.')
else:
    print('Введенной длине волны соответствует', color, 'цвет.')