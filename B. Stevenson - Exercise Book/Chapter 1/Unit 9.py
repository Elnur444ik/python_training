deposit = float(input('Введите сумму первоначального депозита: '))
BET = 1.04
first = deposit * BET
second = first * BET
third = second * BET

print('Сумма на счету в конце первого года:', round(first, 2))
print('Сумма на счету в конце второго года:', round(second, 2))
print('Сумма на счету в конце третьего года:', round(third, 2))
