DAYS = 86400
HOURS = 3600
MINUTES = 60

seconds = int(input('Введите количество секунд: '))

D = seconds / DAYS
seconds = seconds % DAYS

HH = seconds / HOURS
seconds = seconds % HOURS

MM = seconds / MINUTES
SS = seconds % MINUTES

print('Длительность:', '%d:%0.2d:%0.2d:%0.2d:' % (D, HH, MM, SS))
