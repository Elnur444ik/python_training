word = input('Введите оценку в буквенной форме: ')
A_PLUS = 'A+'
A = 'A'
A_MINUS = 'A-'
B_PLUS = 'B+'
B = 'B'
B_MINUS = 'B-'
C_PLUS = 'C+'
C = 'C'
C_MINUS = 'C-'
D_PLUS = 'D+'
D = 'D'
F = 'F'
estimate = -1

if word == A_PLUS:
    estimate = 5
elif word == A:
    estimate = 4
elif word == A_MINUS:
    estimate = 3.7
elif word == B_PLUS:
    estimate = 3.3
elif word == B:
    estimate = 3
elif word == B_MINUS:
    estimate = 2.7
elif word == C_PLUS:
    estimate = 2.3
elif word == C:
    estimate = 2
elif word == C_MINUS:
    estimate = 1.7
elif word == D_PLUS:
    estimate = 1.3
elif word == D:
    estimate = 1
elif word == F:
    estimate = 0

if estimate == -1:
    print('Введено некорректное значение')
else:
    print('Введенной оценке соответствует:', estimate)
