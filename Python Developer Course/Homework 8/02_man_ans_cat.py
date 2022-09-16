# -*- coding: utf-8 -*-

from random import randint

# Доработать практическую часть урока lesson_007/python_snippets/08_practice.py

# Необходимо создать класс кота. У кота есть аттрибуты - сытость и дом (в котором он живет).
# Кот живет с человеком в доме.
# Для кота дом характеризируется - миской для еды и грязью.
# Изначально в доме нет еды для кота и нет грязи.

# Доработать класс человека, добавив методы
#   подобрать кота - у кота появляется дом.
#   купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.
#   убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
# Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу :)

# Кот может есть, спать и драть обои - необходимо реализовать соответствующие методы.
# Когда кот спит - сытость уменьшается на 10
# Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.
# Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5
# Если степень сытости < 0, кот умирает.
# Так же надо реализовать метод "действуй" для кота, в котором он принимает решение
# что будет делать сегодня

# Человеку и коту надо вместе прожить 365 дней.

# -*- coding: utf-8 -*-


# Реализуем модель человека.
# Человек может есть, работать, играть, ходить в магазин.
# У человека есть степень сытости, немного еды и денег.
# Если сытость < 0 единиц, человек умирает.
# Человеку надо прожить 365 дней.
from termcolor import cprint


class Man:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None

    def __str__(self):
        return 'Я - {}, сытость {}'.format(
            self.name, self.fullness)

    def eat(self):
        if self.house.food >= 10:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += 10
            self.house.food -= 10
        else:
            cprint('{} нет еды'.format(self.name), color='red')

    def work(self):
        cprint('{} сходил на работу'.format(self.name), color='blue')
        self.house.money += 210
        self.fullness -= 10

    def watch_MTV(self):
        cprint('{} смотрел MTV целый день'.format(self.name), color='green')
        self.fullness -= 10

    def shopping(self):
        if self.house.money >= 50:
            cprint('{} сходил в магазин за едой'.format(self.name), color='magenta')
            self.house.money -= 50
            self.house.food += 50
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')

    def go_to_the_house(self, house):
        self.house = house
        self.fullness -= 10
        cprint('{} въехал в дом'.format(self.name), color='cyan')

    def pick_up_cat(self, cat, cat_name):
        cat.cat_name = cat_name
        cprint('{} подобрал кота и назвал его {}'.format(self.name, cat.cat_name), color='green')
        cat.house = self.house

    def shopping_cat_food(self):
        if self.house.money >= 50:
            cprint('{} сходил в магазин за кошачьей едой'.format(self.name), color='magenta')
            self.house.cat_food += 50
            self.house.money -= 50
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')

    def house_cleaning(self):
        cprint('{} убирался в доме целый день'.format(self.name), color='green')
        self.house.dirty -= 100
        self.fullness -= 20

    def act(self):
        if self.fullness <= 0:
            cprint('{} умер...'.format(self.name), color='red')
            return
        dice = randint(1, 6)
        if self.fullness < 20 and self.house.food != 0:
            self.eat()
        elif self.house.food < 10 and self.house.money > 50:
            self.shopping()
        elif self.house.cat_food <= 20:
            self.shopping_cat_food()
        elif self.house.money < 50:
            self.work()
        elif self.house.dirty >= 100:
            self.house_cleaning()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.watch_MTV()


class House:

    def __init__(self, house_name):
        self.house_name = house_name
        self.food = 50
        self.money = 50
        self.cat_food = 0
        self.dirty = 0

    def __str__(self):
        return 'В {} еды осталось {}, денег осталось {}, еды для кота {}, грязи {}'.format(
            self.house_name, self.food, self.money, self.cat_food, self.dirty)


class Cat:

    def __init__(self):
        self.house = None
        self.cat_name = None
        self.cat_fullness = 20

    def __str__(self):
        return 'Я - {} (кот), сытость {}'.format(
            self.cat_name, self.cat_fullness)

    def cat_sleeping(self):
        cprint('{} (кот) спал весь день'.format(self.cat_name), color='green')
        self.cat_fullness -= 10

    def cat_eat(self):
        if self.house.cat_food >= 10:
            cprint('{} (кот) поел'.format(self.cat_name), color='yellow')
            self.cat_fullness += 10
            self.house.cat_food -= 10
        else:
            cprint('{} (кот) нет кошачьей еды'.format(self.cat_name), color='red')

    def cat_tear_wallpaper(self):
        cprint('{} (кот) дерёт обои весь день'.format(self.cat_name), color='blue')
        self.house.dirty += 5
        self.cat_fullness -= 10

    def act_cat(self):
        if self.cat_fullness <= 0:
            cprint('{} (кот) умер...'.format(self.cat_name), color='red')
            return
        dice = randint(1, 2)
        if self.cat_fullness < 20 and self.house.cat_food != 0:
            self.cat_eat()
        elif dice == 1:
            self.cat_sleeping()
        elif dice == 2:
            self.cat_eat()
        else:
            self.cat_tear_wallpaper()


elnur = Man(name='Эльнур')
my_sweet_home = House(house_name='Дом(е) Эльнура')
elnur.go_to_the_house(my_sweet_home)
muska = Cat()
lutik = Cat()
elnur.pick_up_cat(cat=muska, cat_name='Муська')
elnur.pick_up_cat(cat=lutik, cat_name='Лютик')
for day in range(1, 366):
    print('================ день {} =================='.format(day))
    elnur.act()
    muska.act_cat()
    lutik.act_cat()
    print('--- в конце дня ---')
    print(elnur)
    print(muska)
    print(lutik)
    print(my_sweet_home)

# Создадим двух людей, живущих в одном доме - Бивиса и Батхеда
# Нужен класс Дом, в нем должн быть холодильник с едой и тумбочка с деньгами
# Еда пусть хранится в холодильнике в доме, а деньги - в тумбочке.


# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.

# (Можно определить критическое количество котов, которое может прокормить человек...)
