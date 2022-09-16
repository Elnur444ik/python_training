# -*- coding: utf-8 -*-

from termcolor import cprint
from random import randint


######################################################## Часть первая
#
# Создать модель жизни небольшой семьи.
#
# Каждый день участники жизни могут делать только одно действие.
# Все вместе они должны прожить год и не умереть.
#
# Муж может:
#   есть,
#   играть в Dota 2,
#   ходить на работу,
# Жена может:
#   есть,
#   покупать продукты,
#   покупать шубу,
#   убираться в доме,

# Все они живут в одном доме, дом характеризуется:
#   кол-во денег в тумбочке (в начале - 100)
#   кол-во еды в холодильнике (в начале - 50)
#   кол-во грязи (в начале - 0)
#
# У людей есть имя, степень сытости (в начале - 30) и степень счастья (в начале - 100).
#
# Любое действие, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Кушают взрослые максимум по 30 единиц еды, степень сытости растет на 1 пункт за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе чел умрет от голода.
#
# Деньги в тумбочку добавляет муж, после работы - 150 единиц за раз.
# Еда стоит 10 денег 10 единиц еды. Шуба стоит 350 единиц.
#
# Грязь добавляется каждый день по 5 пунктов, за одну уборку жена может убирать до 100 единиц грязи.
# Если в доме грязи больше 90 - у людей падает степень счастья каждый день на 10 пунктов,
# Степень счастья растет: у мужа от игры в WoT (на 20), у жены от покупки шубы (на 60, но шуба дорогая)
# Степень счастья не должна падать ниже 10, иначе чел умрает от депресии.
#
# Подвести итоги жизни за год: сколько было заработано денег, сколько сьедено еды, сколько куплено шуб.


class House:

    def __init__(self, house_name):
        self.house_name = house_name
        self.food = 60
        self.money = 100
        self.dirty = 0
        self.cat_food = 30

    def __str__(self):
        return 'В {} еды осталось {}, денег осталось {}, грязи {}, кошачьей еды осталось {}'.format(
            self.house_name, self.food, self.money, self.dirty, self.cat_food)


class Man:

    def __init__(self, name):
        self.name = name
        self.fullness = 30
        self.happiness = 100
        self.all_food = 0
        self.house = None

    def __str__(self):
        if self.happiness < 0:
            self.happiness = 0
        elif self.happiness > 100:
            self.happiness = 100
        if self.fullness > 100:
            self.fullness = 100
        elif self.fullness < 0:
            self.fullness = 0
        return 'Я - {}, сытость {}, счастье {}, '.format(
            self.name, self.fullness, self.happiness)

    def eat(self):
        if self.house.food >= 30:
            self.fullness += 30
            self.house.food -= 30
            self.all_food += 30
            eat = 1
        elif 10 < self.house.food < 30:
            self.fullness += 20
            self.house.food -= 20
            self.all_food += 20
            eat = 1
        elif self.house.food <= 10:
            self.fullness += 10
            self.house.food -= 10
            self.all_food += 10
            eat = 1
        else:
            self.fullness -= 10
            eat = 0

        if eat == 1:
            cprint('{} поел'.format(self.name), color='yellow')
        else:
            cprint('{} нет еды'.format(self.name), color='red')

    def move_into_the_house(self, house):
        self.house = house
        self.fullness -= 10
        cprint('{} въехал в дом'.format(self.name), color='cyan')

    def pick_up_cat(self, cat, cat_name):
        cat.cat_name = cat_name
        cprint('{} подобрал кота и назвал его {}'.format(self.name, cat.cat_name), color='green')
        cat.house = self.house

    def pet_the_cat(self):
        self.fullness -= 10
        self.happiness += 5
        cprint('{} погладил(а) кота'.format(self.name), color='yellow')


class Husband(Man):

    def __init__(self, name):
        super().__init__(name=name)
        self.days_in_dota = 0
        self.all_money = 0

    def __str__(self):
        condition = super().__str__()
        return condition + '{} дней играл в Dota 2'.format(self.days_in_dota)

    def act(self):
        if self.fullness <= 0:
            cprint('{} умер от голода...'.format(self.name), color='red')
            return
        if self.happiness <= 10:
            cprint('{} умер от депрессии...'.format(self.name), color='red')
            return
        dice = randint(1, 5)
        if self.fullness <= 20:
            self.eat()
        elif self.house.money < 50:
            self.work()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        elif dice == 3:
            self.pet_the_cat()
        else:
            self.gaming()

    def work(self):
        cprint('{} сходил на работу'.format(self.name), color='blue')
        self.house.money += 300
        self.fullness -= 10
        self.all_money += 300

    def gaming(self):
        cprint('{} играл в Dota 2 целый день'.format(self.name), color='green')
        self.fullness -= 10
        self.happiness += 20
        self.days_in_dota += 1


class Wife(Man):

    def __init__(self, name):
        super().__init__(name=name)
        self.coats = 0

    def __str__(self):
        condition = super().__str__()
        return condition + '{} шуб(ы)'.format(self.coats)

    def act(self):
        if self.fullness <= 0:
            cprint('{} умерла от голода...'.format(self.name), color='red')
            return
        if self.happiness <= 10:
            cprint('{} умерла от депрессии...'.format(self.name), color='red')
            return
        dice = randint(1, 6)
        if self.fullness < 20:
            self.eat()
        elif self.house.dirty >= 100:
            self.clean_house()
        elif self.house.food <= 30:
            self.shopping()
        elif self.house.cat_food <= 10:
            self.shopping_cat_food()
        elif dice == 1:
            self.shopping()
        elif dice == 2:
            self.eat()
        elif dice == 3:
            self.pet_the_cat()
        elif dice == 4:
            self.shopping_cat_food()
        else:
            self.buy_fur_coat()

    def shopping(self):
        if self.house.money >= 50:
            if self.house.food >= 120:
                new_food = 20
                self.house.money -= 20
                self.house.food += new_food
            elif 50 <= self.house.food <= 120:
                new_food = 35
                self.house.money -= 35
                self.house.food += new_food
            else:
                new_food = 50
                self.house.money -= 50
                self.house.food += new_food
            cprint('{} сходила в магазин и купила {} еды'.format(self.name, new_food), color='magenta')
            self.fullness -= 10
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')

    def shopping_cat_food(self):
        if self.house.money >= 30:
            if self.house.cat_food >= 30:
                new_food = 10
                self.house.money -= 10
                self.house.cat_food += new_food
            elif 10 < self.house.cat_food <= 20:
                new_food = 20
                self.house.money -= 20
                self.house.cat_food += new_food
            else:
                new_food = 30
                self.house.money -= 30
                self.house.cat_food += new_food
            cprint('{} сходила в магазин и купила коту {} еды'.format(self.name, new_food), color='magenta')
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')
        self.fullness -= 10

    def buy_fur_coat(self):
        if self.house.money >= 400:
            self.coats += 1
            self.fullness -= 10
            self.happiness += 60
            self.house.money -= 350
            cprint('{} купила шубу'.format(self.name), color='green')
        else:
            cprint('У {} нет денег на шубу'.format(self.name), color='green')

    def clean_house(self):
        self.fullness -= 10
        self.house.dirty -= 100
        if self.house.dirty < 0:
            self.house.dirty = 0
        cprint('{} убиралась в доме целый день'.format(self.name), color='green')

    def give_a_birth_to_a_baby(self, child, name):
        child.name = name
        cprint('{} родила {}'.format(self.name, child.name), color='green')
        child.house = self.house


class Cat:

    def __init__(self):
        self.house = None
        self.cat_name = None
        self.cat_fullness = 20
        self.days_tear = 0
        self.all_cat_food = 0

    def __str__(self):
        return 'Я - {} (кот), сытость {}'.format(
            self.cat_name, self.cat_fullness)

    def act(self):
        if self.cat_fullness <= 0:
            cprint('{} (кот) умер от голода...'.format(self.cat_name), color='red')
            return
        dice = randint(1, 4)
        if self.cat_fullness < 20:
            self.eat()
        elif dice == 1:
            self.sleep()
        elif dice == 2:
            self.eat()
        else:
            self.cat_tear_wallpaper()

    def eat(self):
        if self.house.cat_food >= 10:
            cprint('{} (кот) поел'.format(self.cat_name), color='yellow')
            self.cat_fullness += 20
            self.house.cat_food -= 10
            self.all_cat_food += 10
        else:
            self.cat_fullness -= 10
            cprint('{} (кот) нет кошачьей еды'.format(self.cat_name), color='red')

    def sleep(self):
        cprint('{} (кот) спал весь день'.format(self.cat_name), color='green')
        self.cat_fullness -= 10

    def cat_tear_wallpaper(self):
        cprint('{} (кот) дерёт обои весь день'.format(self.cat_name), color='blue')
        self.house.dirty += 5
        self.cat_fullness -= 10
        self.days_tear += 1


class Child(Man):

    def __init__(self):
        super().__init__(self)
        self.house = None
        self.name = None
        self.days_sleep = 0

    def sleep(self):
        self.days_sleep += 1
        cprint('{} спала весь день'.format(self.name), color='green')
        self.fullness -= 10

    def eat(self):
        if self.house.food >= 10:
            self.fullness += 10
            self.house.food -= 10
            self.all_food += 10
            cprint('{} поела'.format(self.name), color='yellow')
        else:
            self.fullness -= 10
            cprint('{} нет еды'.format(self.name), color='red')

    def act(self):
        if self.fullness <= 0:
            cprint('{} умерла от голода...'.format(self.name), color='red')
            return
        dice = randint(1, 2)
        if self.fullness <= 20:
            self.eat()
        elif dice == 1:
            self.sleep()
        else:
            self.eat()

    def move_into_the_house(self, house):
        pass

    def pick_up_cat(self, cat, cat_name):
        pass

    def pet_the_cat(self):
        pass


home = House(house_name='Дом(е) Эльнура и Марии')
elnur = Husband(name='Эльнур')
mariya = Wife(name='Мария')
muska = Cat()
yagmur = Child()
elnur.move_into_the_house(home)
mariya.move_into_the_house(home)
elnur.pick_up_cat(muska, cat_name='Муська')
mariya.give_a_birth_to_a_baby(yagmur, 'Ягмур')

for day in range(1, 366):
    cprint('================== День {} =================='.format(day), color='red')
    elnur.act()
    mariya.act()
    yagmur.act()
    muska.act()
    home.dirty += 5
    if home.dirty >= 90:
        elnur.happiness -= 10
        mariya.happiness -= 10
    cprint(elnur, color='cyan')
    cprint(mariya, color='cyan')
    cprint(yagmur, color='cyan')
    cprint(muska, color='cyan')
    cprint(home, color='cyan')
cprint('================== Статистика за год =================='.format(day), color='red')
cprint(
    '{money} денег было заработано, {days} дней {husband} играл в доту, '
    '{coasts} шуб купила {wife}, {days_sleep} дней спала {child},{days_tear} дней {cat}(кот) драл обои, '
    '{husband} {husband_food} съел еды, {wife} {wife_food} cъела еды, {child} {child_food} съела еды, {cat}(кот) '
    '{cat_food} съел кошачьей еды'.format(money=elnur.all_money, days=elnur.days_in_dota, husband=elnur.name,
                                          coasts=mariya.coats, wife=mariya.name, husband_food=elnur.all_food,
                                          wife_food=mariya.all_food, days_sleep=yagmur.days_sleep,
                                          child_food=yagmur.all_food, child=yagmur.name, days_tear=muska.days_tear,
                                          cat_food=muska.all_cat_food, cat=muska.cat_name), color='green')

######################################################## Часть вторая
#
# После подтверждения учителем первой части надо
# отщепить ветку develop и в ней начать добавлять котов в модель семьи
#
# Кот может:
#   есть,
#   спать,
#   драть обои
#
# Люди могут:
#   гладить кота (растет степень счастья на 5 пунктов)
#   Еда для кота покупается за деньги: за 10 денег 10 еды.
#
# В доме добавляется:
#   еда для кота (в начале - 30)
#
# У кота есть имя и степень сытости (в начале - 30)
# Любое действие кота, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Кушает кот максимум по 10 единиц еды, степень сытости растет на 2 пункта за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе кот умрет от голода.
#
# Если кот дерет обои, то грязи становится больше на 5 пунктов


######################################################## Часть вторая бис
#
# После реализации первой части надо в ветке мастер продолжить работу над семьей - добавить ребенка
#
# Ребенок может:
#   есть,
#   спать,
#
# отличия от взрослых - кушает максимум 10 единиц еды,
# степень счастья  - не меняется, всегда ==100 ;)


######################################################## Часть третья
#
# после подтверждения учителем второй части (обоих веток)
# влить в мастер все коммиты из ветки develop и разрешить все конфликты
# отправить на проверку учителем.


# home = House()
# serge = Husband(name='Сережа')
# masha = Wife(name='Маша')
# kolya = Child(name='Коля')
# murzik = Cat(name='Мурзик')
#
# for day in range(365):
#     cprint('================== День {} =================='.format(day), color='red')
#     serge.act()
#     masha.act()
#     kolya.act()
#     murzik.act()
#     cprint(serge, color='cyan')
#     cprint(masha, color='cyan')
#     cprint(kolya, color='cyan')
#     cprint(murzik, color='cyan')

# Усложненное задание (делать по желанию)
#
# Сделать из семьи любителей котов - пусть котов будет 3, или даже 5-10.
# Коты должны выжить вместе с семьей!
#
# Определить максимальное число котов, которое может прокормить эта семья при значениях зарплаты от 50 до 400.
# Для сглаживание случайностей моделирование за год делать 3 раза, если 2 из 3х выжили - считаем что выжили.
#
# Дополнительно вносить некий хаос в жизнь семьи
# - N раз в год вдруг пропадает половина еды из холодильника (коты?)
# - K раз в год пропадает половина денег из тумбочки (муж? жена? коты?!?!)
# Промоделировать - как часто могут случаться фейлы что бы это не повлияло на жизнь героев?
#   (N от 1 до 5, K от 1 до 5 - нужно вычислит максимумы N и K при котором семья гарантированно выживает)
#
# в итоге должен получится приблизительно такой код экспериментов
# for food_incidents in range(6):
#   for money_incidents in range(6):
#       life = Simulation(money_incidents, food_incidents)
#       for salary in range(50, 401, 50):
#           max_cats = life.experiment(salary)
#           print(f'При зарплате {salary} максимально можно прокормить {max_cats} котов')
