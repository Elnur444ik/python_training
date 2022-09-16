PRICE_BREAD = 3.49
DISCOUNT = 0.6

number_bread = int(input('Введите количество купленного вчерашнего хлеба: '))

price_disc = PRICE_BREAD * (1 - DISCOUNT)

price = number_bread * price_disc

print('Стоимость хлеба: $%5.2f' % PRICE_BREAD)
print('Стоимость хлеба со скидкой: $%5.2f' % price_disc)
print('Стоимость приобретенного вчерашнего хлеба: $%5.2f' % price)