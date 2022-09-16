car_number = input('Введите номер машины: ')

numbers = car_number[3:]
lenght = len(numbers)
if numbers.isdigit():
    if lenght == 3:
        print('Номер старого образца.')
    elif lenght == 4:
        print('Номер нового образца.')
    else:
        print('Введено некорректное значение.')
else:
    print('Введено некорректное значение.')
