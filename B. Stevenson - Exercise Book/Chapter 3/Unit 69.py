age = input('Введите возраст (пустое поле для выхода): ')
total_cash = 0

while age != '':
    age = int(age)
    if age <= 2:
        ticket_price = 0
    elif 3 <= age <= 12:
        ticket_price = 14
    elif age > 65:
        ticket_price = 18
    else:
        ticket_price = 23

    total_cash += ticket_price
    age = input('Введите возраст (пустое поле для выхода): ')

print('Стоимость билетов группы: ', total_cash)



