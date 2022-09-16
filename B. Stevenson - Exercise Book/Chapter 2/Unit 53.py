estimate = int(input('Введите оценку в буквенной форме: '))
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
word = ' '

if 4 < estimate <= 5:
    word = A_PLUS
elif estimate == 4:
    word = A
elif estimate == A_MINUS:
    word = A_MINUS
elif estimate == B_PLUS:
    word = B_PLUS
elif estimate == B:
    word = B
elif estimate == B_MINUS:
    word = B_MINUS
elif estimate == C_PLUS:
    word = C_PLUS
elif estimate == C:
    word = C
elif estimate == C_MINUS:
    word = C_MINUS
elif estimate == D_PLUS:
    word = D_PLUS
elif estimate == D:
    word = D
elif estimate == F:
    word = F

if estimate == -1:
    print('Введено некорректное значение')
else:
    print('Введенной оценке соответствует:', estimate)
