binary_number = input('Введите двоичное число: ')
decimal_number = 0
pos=0
check = 0
binary_number = binary_number[::-1]
for number in binary_number:
    if number == '1':
        decimal_number += 2 ** pos
        pos += 1
    elif number == '0':
        pos += 1
        pass
    else:
        print('Введено некорректное значение')
        check = 1
        break

if check == 0:
    print('В десятичном виде равно: ', decimal_number)


