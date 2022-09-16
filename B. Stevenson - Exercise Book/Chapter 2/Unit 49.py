year = int(input('Введите год: '))
animal = ' '
year_animal = year % 12
if year_animal == 8:
    animal = 'дракона'
elif year_animal == 9:
    animal = 'змеи'
elif year_animal == 10:
    animal = 'лошади'
elif year_animal == 11:
    animal = 'козы'
elif year_animal == 0:
    animal = 'обезьяны'
elif year_animal == 1:
    animal = 'петуха'
elif year_animal == 2:
    animal = 'собаки'
elif year_animal == 3:
    animal = 'свиньи'
elif year_animal == 4:
    animal = 'крысы'
elif year_animal == 5:
    animal = 'быка'
elif year_animal == 6:
    animal = 'тигра'
elif year_animal == 7:
    animal = 'кролика'

print('Этот год является годом', animal)
