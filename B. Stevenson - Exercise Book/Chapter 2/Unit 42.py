note = input('Введите ноту: ')
octave_number = int(input('Введите номер нотации октавы: '))
note = note.upper()
note_table = 0
C4 = 261.63
D4 = 293.66
E4 = 329.63
F4 = 349.23
G4 = 392.00
A4 = 440.00
B4 = 493.88

if note == 'C':
    note_table = C4
elif note == 'D':
    note_table = D4
elif note == 'E':
    note_table = E4
elif note == 'F':
    note_table = F4
elif note == 'G':
    note_table = G4
elif note == 'A':
    note_table = A4
elif note == 'B':
    note_table = B4

if note_table != 0:
    freq = note_table * 2 ** (4 - octave_number)
    print('Частота введенной ноты:', freq)
else:
    print('Введено некорректное значение')
