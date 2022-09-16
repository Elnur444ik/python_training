amount = float(input('Введите сумму заказа: $ '))

tax = 0.13 * amount
tip = amount * 0.18
TaxAndTip = tax + tip
print('Сумма налога:$%.2f' % tax)

print('Сумма чаевых:$%.2f' % tip)

print('Общая сумма издержек:$%.2f' % TaxAndTip)
