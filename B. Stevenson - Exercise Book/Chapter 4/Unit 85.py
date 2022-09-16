a_side = float(input('Введите значение первого катета : '))
b_side = float(input('Введите значение второго катета: '))


def hypotenuse(a, b):
    global hypo
    hypo = (a ** 2 + b ** 2) ** .5


hypotenuse(a_side, b_side)
print('Гипотенуза равна', hypo)
