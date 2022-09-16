letter = input('Введите букву: ')
vowels = ['a', 'e', 'i', 'o', 'u']
if letter in vowels:
    print('Буква гласная')
elif letter == 'y':
    print('Может быть как гласная, так и согласная')
else:
    print('Буква согласная')
