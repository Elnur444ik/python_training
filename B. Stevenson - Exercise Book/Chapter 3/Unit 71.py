pi_number = '3'
number_1 = 2
number_2 = 3
number_3 = 4
n = 1
while len(pi_number) < 15:
    pi_number = float(pi_number)
    pi_number += 4 / (number_1 * number_2 * number_3)
    pi_number = round(pi_number, n)
    n += 1
    number_1 += 2
    number_2 += 2
    number_3 += 2
    pi_number = str(pi_number)
print(pi_number)