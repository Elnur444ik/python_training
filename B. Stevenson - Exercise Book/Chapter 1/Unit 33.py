first_number = int(input('Введите первое число: '))
second_number = int(input('Введите второе число: '))
third_number = int(input('Введите третье число: '))

number_sum = first_number + second_number + third_number
number_max = max(first_number, second_number, third_number)
number_min = min(first_number, second_number, third_number)

second = number_sum - number_max - number_min

print('Отсортированные числа:', number_min, ',', second, ',', number_max)
