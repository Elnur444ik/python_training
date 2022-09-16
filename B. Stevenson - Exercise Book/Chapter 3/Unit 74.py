x = float(input('Введите число: '))
guess = x / 2
while (guess * guess) - x >= 10 ** -12:
    guess = (guess + x / guess) / 2

print('Корень равен: ', guess)