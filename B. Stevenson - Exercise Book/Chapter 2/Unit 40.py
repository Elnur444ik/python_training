noize = float(input('Введите уровень шума от 40 до 130 в дБ: '))

if noize < 40:
    print('Введеное значение ниже минимального')
elif noize == 40:
    print('Введеное значение соответствует уровню шума в тихой комнате')
elif 40 < noize < 70:
    print('Введеное значение соответствует уровню шума между тихой комнатой и будильником')
elif noize == 70:
    print('Введеное значение соответствует уровню шума будильника')
elif 70 < noize < 106:
    print('Введеное значение соответствует уровню шума между будильником и газовой газонокосилкой')
elif noize == 106:
    print('Введеное значение соответствует уровню шума газовой газонокосилки')
elif 106 < noize < 130:
    print('Введеное значение соответствует уровню шума между газовой газонокосилкой и отбойным молотком')
elif noize == 130:
    print('Введеное значение соответствует уровню шума отбойного молотка')
else:
    print('Введенное значение выше максимального')