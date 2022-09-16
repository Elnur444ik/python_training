age = int(input('Введите возраст по-человеческим меркам: '))
age_dog = 0
if age < 0:
    print('Возраст не может быть меньше нуля')
elif 0 < age <= 2:
    age_dog = 10.5 * age
    print('Возраст по-собачьи:', age_dog)
else:
    age_dog = 21 + (age - 2) * 4
    print('Возраст по-собачьи:', age_dog)
