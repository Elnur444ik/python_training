word = input('Введите слово: ')
is_palindrome = True
i = 0
while i < len(word) / 2 and is_palindrome:
    if word[i] != word[len(word) - i - 1]:
        is_palindrome = False
    i = i + 1

if is_palindrome:
    print('Это полиндром')
else:
    print('Это не полиндром')

