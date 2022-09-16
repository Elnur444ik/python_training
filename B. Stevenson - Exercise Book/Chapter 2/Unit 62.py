from random import choice

red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
parity = ' '
range_number = ' '
color = ' '
roulette_number = choice(range(0, 38))

if roulette_number == 37:
    roulette_number = '00'

if roulette_number != 0 and roulette_number != '00':
    if roulette_number in red:
        color = 'красное'
    else:
        color = 'черное'

if roulette_number != 0 and roulette_number != '00':
    if roulette_number % 2 == 0:
        parity = 'четное'
    else:
        parity = 'нечетное'

if roulette_number != 0 and roulette_number != '00':
    if roulette_number in range(1, 19):
        range_number = 'от 1 до 18'
    else:
        range_number = '19 до 36'

print('Выпавший номер:', roulette_number, '...')

print('Выигравшая ставка:', roulette_number)

if roulette_number != 0 and roulette_number != '00':
    print('Выигравшая ставка:', color)
    print('Выигравшая ставка:', parity)
    print('Выигравшая ставка:', range_number)
