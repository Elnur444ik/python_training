message = input('Введите сообщение: ')
shift = int(input('Введите сдвиг: '))
new_message = ''
for ch in message:
    if ch >= 'а' and ch <= 'я':
        pos = ord(ch) - ord('а')
        pos = (pos + shift) % 33
        new_char = chr(pos + ord('а'))
        new_message = new_message + new_char
    elif ch >= 'А' and ch <= 'Я':
        pos = ord(ch) - ord('А')
        pos = (pos + shift) % 33
        new_char = chr(pos + ord('А'))
        new_message = new_message + new_char
    else:
        new_message = new_message + ch

print('Новое сообщение:', new_message)

