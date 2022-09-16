base_cost = 10.95
add_cost = 2.95

number_goods = int(input('Введите количество товаров в заказе: '))


def shipping_cost(goods):
    if goods > 0:
        cost = base_cost + add_cost * (goods - 1)
        print('Стоимость дсотавки равна: $', round(cost, 2))
    else:
        print('Количество товаров в заказе введенно некорректно')


shipping_cost(number_goods)
