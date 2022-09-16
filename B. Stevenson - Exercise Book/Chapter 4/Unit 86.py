base_rate = 4
add_rate = 0.25

distance = float(input('Введите пройденное расстояние в километрах: '))


def cost(distance):
    cost = base_rate + (distance * 1000 / 140) * add_rate
    print('Стоимость поездки равна: $', round(cost, 2))


cost(distance)
