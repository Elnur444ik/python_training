cents_200 = 200
cents_100 = 100
cents_25 = 25
cents_10 = 10
cents_5 = 5

cents = int(input('Введите сумму в центах: '))

print('', cents//cents_200, 'двухдолларовых монет')
cents = cents % cents_200

print('', cents//cents_100, 'однодолларовых монет')
cents = cents % cents_100

print('', cents//cents_25, '25-центовых монет')
cents = cents % cents_25

print('', cents//cents_10, '10-центоваых монет')
cents = cents % cents_10

print('', cents//cents_5, '5-центовых монет')
cents = cents % cents_5

print('', cents, 'центов')
