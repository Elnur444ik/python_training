# -*- coding: utf-8 -*-

# (цикл while)

# Ежемесячная стипендия студента составляет educational_grant руб., а расходы на проживание превышают стипендию
# и составляют expenses руб. в месяц. Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца
# Составьте программу расчета суммы денег, которую необходимо единовременно попросить у родителей,
# чтобы можно было прожить учебный год (10 месяцев), используя только эти деньги и стипендию.
# Формат вывода:
#   Студенту надо попросить ХХХ.ХХ рублей

educational_grant, expenses = 10000, 12000
months = 10
step_month = 1
last_expenses = 12000
while step_month < 10:
    step_month += 1
    last_expenses = last_expenses * 1.03
    expenses = expenses + last_expenses

monetary_assistant = expenses - educational_grant * months
print('Студенту надо попросить', round(monetary_assistant, 2), 'рублей')
