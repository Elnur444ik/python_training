nom_val = int(input('Введите номинал банкноты: '))
president = ' '
if nom_val == 1:
    president = 'Джордж Вашингтон'
elif nom_val == 2:
    president = 'Томас Джефферсон'
elif nom_val == 5:
    president = 'Авраам Линкольн'
elif nom_val == 10:
    president = 'Александр Гамильтон'
elif nom_val == 20:
    president = 'Эндрю Джексон'
elif nom_val == 50:
    president = 'Улисс Грант'
elif nom_val == 100:
    president = 'Бенджамин Франклин'
if president == ' ':
    print('Такого номинала не существует')
else:
    print('На банкноте изображен:', president)