PSI_CONST = 0.145
MM_CONST = 7.50064
ATM_CONST = 0.0099

kPa = float(input('Введите давление в кПа: '))

PSI = kPa * PSI_CONST

MM = kPa * MM_CONST

ATM = kPa * ATM_CONST

print('Давление в фунтах на квадратный дюйм:', round(PSI, 2))

print('Давление в миллиметрах ртутного столба::', round(MM, 2))

print('Давление в атмосферах:', round(ATM, 2))
