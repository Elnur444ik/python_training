first_side = float(input('Введите значение первой стороны треугольника '))
second_side = float(input('Введите значение второй стороны треугольника '))
third_side = float(input('Введите значение третьей стороны треугольника '))

if first_side == second_side == third_side:
    print('Треугольник равносторонний')
elif first_side != second_side != third_side:
    print('Треугольник разносторонний')
elif first_side == second_side or first_side == third_side or second_side == third_side:
    print('Треугольник равнобедренный')
