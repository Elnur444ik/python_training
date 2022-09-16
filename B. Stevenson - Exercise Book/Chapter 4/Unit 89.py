def numeral(x):
    if x == 1:
        word = 'First'
    elif x == 2:
        word = 'Second'
    elif x == 3:
        word = 'Third'
    elif x == 4:
        word = 'Fourth'
    elif x == 5:
        word = 'Fifth'
    elif x == 6:
        word = 'Sixth'
    elif x == 7:
        word = 'Seventh'
    elif x == 8:
        word = 'Eighth'
    elif x == 9:
        word = 'Ninth'
    elif x == 10:
        word = 'Tenth'
    elif x == 11:
        word = 'Eleventh'
    elif x == 12:
        word = 'Twelfth'
    else:
        pass
    return word


def main():
    for i in range(1, 12):
        print(numeral(i))


main()
