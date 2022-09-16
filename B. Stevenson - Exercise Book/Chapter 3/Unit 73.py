message = input('Введите сообщение: ')
shift = int(input('Введите сдвиг: '))
new_message = ''
for ch in message:
    if ch >= 'a' and ch <= 'z':
        pos = ord(ch) - ord('a')
        pos = (pos + shift) % 26
        new_char = chr(pos + ord('a'))
        new_message = new_message + new_char
    elif ch >= 'A' and ch <= 'Z':
        pos = ord(ch) - ord('A')
        pos = (pos + shift) % 26
        new_char = chr(pos + ord('A'))
        new_message = new_message + new_char
    else:
        new_message = new_message + ch

print('Новое сообщение:', new_message)

