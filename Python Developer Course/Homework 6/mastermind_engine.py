hidden_number = ''


def number():
    from random import randint
    first_number = randint(1, 9)
    global hidden_number
    hidden_number += str(first_number)
    while len(hidden_number) < 4:
        check = None
        other_numbers = randint(0, 9)
        for symbol in hidden_number:
            if other_numbers == int(symbol):
                check = 0
        if check == 0:
            del other_numbers
        else:
            hidden_number += str(other_numbers)
    return hidden_number


bulls = 0
cows = 0


def check_number(computer_number, user_number):
    global bulls, cows
    bulls = 0
    cows = 0
    for symbol in range(0, 4):
        if computer_number[symbol] == user_number[symbol]:
            bulls += 1
    for computer_symbol in computer_number:
        for number_symbol in user_number:
            if computer_symbol == number_symbol:
                cows += 1
    cows -= bulls
    return bulls, cows

