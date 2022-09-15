# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join
live_in_the_area = []
separator = ', '
from district.central_street.house1 import room1, room2
live_in_the_area += room1.folks
live_in_the_area += room2.folks

from district.central_street.house2 import room1, room2
live_in_the_area += room1.folks
live_in_the_area += room2.folks

from district.soviet_street.house1 import room1, room2
live_in_the_area += room1.folks
live_in_the_area += room2.folks

from district.soviet_street.house2 import room1, room2
live_in_the_area += room1.folks
live_in_the_area += room2.folks


print('На районе живут:', separator.join(live_in_the_area))


