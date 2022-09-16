from random import randint

number_max = randint(1, 100)
print(number_max, '==> Обновление')
count_max = 0
for i in range(1, 100):
    number = randint(1, 100)
    if number > number_max:
        number_max = number
        count_max += 1
        print(number_max, '==> Обновление')
    else:
        print(number)

print('Максимальное число в ряду:', number_max)
print('Количество смен максимального значения:', count_max)

