position = input('Введите оозицию на шахматной доске: ')
first_color = 0
word = position[0]
number = int(position[1])
black_word = ['a', 'c', 'e', 'g']
white_word = ['b', 'd', 'f', 'h']
if word in black_word:
    first_color = 0
elif word in white_word:
    first_color = 1
second_color = first_color + number
if second_color % 2 == 0:
    print('Белая позиция')
else:
    print('Черная позиция')
