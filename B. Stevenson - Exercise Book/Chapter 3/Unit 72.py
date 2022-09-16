answer = ''
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        answer = 'Fizz-Buzz'
    elif number % 5 == 0:
        answer = 'Buzz'
    elif number % 3 == 0:
        answer = 'Fizz'
    else:
        answer = number
    print(number, ':', answer)


