price = input('Введите целое число (пустое поле для выхода): ')
total = 0

while price != '':
    total = total + float(price)
    price = input('Введите целое число (пустое поле для выхода): ')
print('Полная сумма к оплате:', total)

rounding = total * 100 % 5
if rounding < 2.5:
    cash_total = total - rounding / 100
else:
    cash_total = total + 0.05 - rounding / 100

print('Сумма для оплаты наличными:', cash_total)
