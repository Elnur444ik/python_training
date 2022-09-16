shake = float(input('Введите магнитуду землетрясения: '))
level = ' '

if shake < 2:
    level = 'минимальный'
elif 2 <= shake < 3:
    level = 'очень слабый'
elif 3 <= shake < 4:
    level = 'слабый'
elif 4 <= shake < 5:
    level = 'промежуточный'
elif 5 <= shake < 6:
    level = 'умеренный'
elif 6 <= shake < 7:
    level = 'сильный'
elif 7 <= shake < 8:
    level = 'очень сильный'
elif 8 <= shake < 10:
    level = 'огромный'

elif shake > 10:
    level = 'разрушительный'

print('Уровень введенного землетрясения:', level)
