minutes = int(input('Введите количество израсходованных минут: '))
sms = int(input('Введите количество отправдленных смс: '))
TAX_911 = 0.44
MINUTES_RATE = 0.25
SMS_RATE = 0.15
TAX_RATE = 0.05
COST_TARIFF = 15
if minutes > 50:
    minutes_bill = (minutes - 50) * MINUTES_RATE
else:
    minutes_bill = 0

if sms > 50:
    sms_bill = (sms - 50) * SMS_RATE
else:
    sms_bill = 0

tax = (COST_TARIFF + minutes_bill + sms_bill + TAX_911) * TAX_RATE

total = COST_TARIFF + minutes_bill + sms_bill + TAX_911 + tax

print('Базовая стоимость тарифа: $', COST_TARIFF)

if minutes_bill != 0:
    print('Сумма за дополнительные минуты: $', minutes_bill)

if sms_bill != 0:
    print('Сумма за дополнительные смс: $', sms_bill)

print('Сумма отчислений колл-центрам 911: $', TAX_911)

print('Сумма налога: $', round(tax, 2))

print('Итоговая сумма к оплате: $', round(total, 2))
