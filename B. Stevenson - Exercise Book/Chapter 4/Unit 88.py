def mediana(first, second, third):
    summary = first + second + third
    medi = summary - max(first, second, third) - min(first, second, third)
    return medi


def main():
    first_number = float(input('Введите первое число: '))
    second_number = float(input('Введите второе число: '))
    third_number = float(input('Введите третье число: '))
    print('Медиана равна: ', mediana(first_number, second_number, third_number))


main()
