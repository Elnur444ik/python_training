# -*- coding: utf-8 -*-

# С помощью JSON файла rpg.json задана "карта" подземелья.
# Подземелье было выкопано монстрами и они всё ещё скрываются где-то в его глубинах,
# планируя набеги на близлежащие поселения.
# Само подземелье состоит из двух главных разветвлений и нескольких развилок,
# и лишь один из путей приведёт вас к главному Боссу
# и позволит предотвратить набеги и спасти мирных жителей.

# Напишите игру, в которой пользователь, с помощью консоли,
# сможет:
# 1) исследовать это подземелье:
#   -- передвижение должно осуществляться присваиванием переменной и только в одну сторону
#   -- перемещаясь из одной локации в другую, пользователь теряет время, указанное в конце названия каждой локации
# Так, перейдя в локацию Location_1_tm500 - вам необходимо будет списать со счёта 500 секунд.
# Тег, в названии локации, указывающий на время - 'tm'.
#
# 2) сражаться с монстрами:
#   -- сражение имитируется списанием со счета персонажа N-количества времени и получением N-количества опыта
#   -- опыт и время указаны в названиях монстров (после exp указано значение опыта и после tm указано время)
# Так, если в локации вы обнаружили монстра Mob_exp10_tm20 (или Boss_exp10_tm20)
# необходимо списать со счета 20 секунд и добавить 10 очков опыта.
# Теги указывающие на опыт и время - 'exp' и 'tm'.
# После того, как игра будет готова, сыграйте в неё и наберите 280 очков при положительном остатке времени.

# По мере продвижения вам так же необходимо вести журнал,
# в котором должна содержаться следующая информация:
# -- текущее положение
# -- текущее количество опыта
# -- текущая дата (отсчёт вести с первой локации с помощью datetime)
# После прохождения лабиринта, набора 280 очков опыта и проверки на остаток времени (remaining_time > 0),
# журнал необходимо записать в csv файл (назвать dungeon.csv, названия столбцов взять из field_names).


# Пример лога игры:
# Вы находитесь в Location_0_tm0
# У вас 0 опыта и осталось 1234567890.0987654321 секунд
# Прошло уже 0:00:00
# Внутри вы видите:
# -- Монстра Mob_exp10_tm0
# -- Вход в локацию: Location_1_tm10400000
# -- Вход в локацию: Location_2_tm333000000
# Выберите действие:
# 1.Атаковать монстра
# 2.Перейти в другую локацию
# 3.Выход
import re
import time
import csv
import json


# если изначально не писать число в виде строки - теряется точность!


class Dungeon:
    re_location = r'Location_(B\d|\d+)_tm(\d+\.\d+|\d+)'
    re_mob = r'(Mob|Boss|Boss\d+)_exp\d+_tm\d+'
    re_time = r'tm\d+'
    re_experience = r'exp\d+'

    def __init__(self, json_file):
        self.json_file = json_file
        self.locations = {}
        self.location_mobs = []
        self.next_locations = []
        self.location_values = []
        self.remaining_time = '1234567890.0987654321'
        self.current_experience = 0
        self.current_date = '0:00:00'
        self.current_location = ''
        self.user_choice = None
        self.start_time = None

    def open_json_file(self):
        with open(self.json_file, 'r') as json_file:
            self.locations = json.load(json_file)
        # первое местоположение
        self.current_location = re.search(self.re_location, *self.locations.keys()).group()
        self.start_time = time.monotonic()

    def mob_search(self, mob):
        location_mob = re.search(self.re_mob, mob)
        if location_mob is not None:
            location_mob = location_mob.group()
            self.location_mobs.append(location_mob)

    def game_log(self):
        # лог игры:
        print('-----------------------------------------------------')
        print(f'Вы находитесь в {self.current_location}.')
        print(f'У вас {self.current_experience} опыта и осталось {self.remaining_time} секунд.')
        self.current_date = time.monotonic() - self.start_time
        self.current_date = time.gmtime(self.current_date)
        self.current_date = time.strftime('%H:%M:%S', self.current_date)
        print(f'Прошло уже {self.current_date} секунд.')
        if self.location_mobs or self.next_locations:
            print(f'Внутри вы видите:')
            for mob in self.location_mobs:
                print(f'-- Монстра/босса {mob}')
            for location in self.next_locations:
                print(f'-- Локацию {location}')
        else:
            print('В этой локации не осталось монстров/боссов и нет переходов в другие локации.'
                  ' Это конец игры. Для выхода нажмите - 3.')

    def user_choice_func(self):
        # Выбор действия
        print('Выберите действие:')
        print('1 - Атаковать монстра/босса')
        print('2 - Перейти в другую локацию')
        print('3 - Выход из игры')
        try:
            self.user_choice = int(input('Действие: '))
        except ValueError:
            pass
        choice_flag = False
        while choice_flag is False:
            if self.user_choice in range(1, 4):
                choice_flag = True
            else:
                print('Значение введено некорректно. Попробуйте еще раз.')
                try:
                    self.user_choice = int(input('Действие: '))
                except ValueError:
                    pass

    def attack_the_monster(self):
        if self.location_mobs:
            print('Выберите монстра/босса, которого хотите атаковать:')
            mob_position = 0
            for mob in self.location_mobs:
                mob_position += 1
                # mob_number = self.location_mobs.index(mob) + 1
                print(f'{mob_position}. Монстр/босс {mob}')
            user_choice = 0
            try:
                user_choice = int(input('Номер монстра/босса: '))
            except ValueError:
                pass
            choice_flag = False
            while choice_flag is False:
                if user_choice in range(1, mob_position + 1):
                    choice_flag = True
                else:
                    print('Значение введено некорректно. Попробуйте еще раз.')
                    try:
                        user_choice = int(input('Номер монстра/босса: '))
                    except ValueError:
                        pass
            mob_experience = re.search(self.re_experience, self.location_mobs[user_choice - 1]).group()
            mob_time = re.search(self.re_time, self.location_mobs[user_choice - 1]).group()
            mob_experience = int(mob_experience[3:])
            mob_time = int(mob_time[2:])
            self.current_experience += mob_experience
            self.remaining_time = float(self.remaining_time) - mob_time

            self.location_mobs.pop(user_choice - 1)
            print(f'Вы победили монстра/босса затратив {mob_time} времени и получив {mob_experience} опыта')
        else:
            print(f'В данной локации нет монстров/боссов. Переходите в другую.')
            # момент выбора следующей локации

    def moving_to_the_next_location(self):
        if self.next_locations:
            print('Выберите локацию, в которую хотите перейти:')
            location_position = 0
            for location in self.next_locations:
                location_position += 1
                print(f'{location_position}. Локация {location}')
            user_choice = 0
            try:
                user_choice = int(input('Номер локации: '))
            except ValueError:
                pass
            choice_flag = False
            while choice_flag is False:
                if user_choice in range(1, location_position + 1):
                    choice_flag = True
                else:
                    print('Значение введено некорректно. Попробуйте еще раз.')
                    try:
                        user_choice = int(input('Номер локации: '))
                    except ValueError:
                        pass
            location = self.next_locations[user_choice - 1]

            # print(self.locations[self.current_location])

            for obj in self.locations[self.current_location]:
                if type(obj) is type(dict()):
                    if location == [*obj.keys()][0]:
                        index = self.locations[self.current_location].index(obj)
                        self.locations = self.locations[self.current_location][index]

            self.current_location = location
            location_time = re.search(self.re_time, location).group()
            location_time = int(location_time[2:])
            self.remaining_time = float(self.remaining_time) - location_time
        else:
            print('Нет переходов в другие локации - тупик. Для выхода из игры нажмите - 3.')

    def setting_new_location(self):
        # мобы и след. локации
        self.location_values = [*self.locations.values()]

        self.location_mobs = []
        self.next_locations = []

        for _ in self.location_values:
            for obj in _:
                if type(obj) is type(str()):
                    self.mob_search(obj)
                elif type(obj) is type(dict()):
                    next_location = re.search(self.re_location, *obj.keys()).group()
                    self.next_locations.append(next_location)
                else:
                    for mob in obj:
                        self.mob_search(mob)

    def exit_game(self):
        if self.current_experience >= 280:
            player_name = input('Вы успешно прошли лабиринт! Введите Ваше имя для записи результата: ')
            field_names = [player_name, self.current_location, self.current_experience, self.current_date]
            with open('dungeon.csv', 'a') as out_csv:
                writer = csv.writer(out_csv, delimiter=';')
                writer.writerow(field_names)
        else:
            print(f'К сожалению вы набрали меньше минимального порога опыта.')
            print('Конец игры.')

    def main(self):
        self.open_json_file()
        self.setting_new_location()
        while float(self.remaining_time) >= 0:
            self.game_log()
            self.user_choice_func()
            if self.user_choice == 1:
                self.attack_the_monster()
                continue
            elif self.user_choice == 2:
                self.moving_to_the_next_location()
                self.setting_new_location()
                continue
            elif self.user_choice == 3:
                self.exit_game()
                break

        else:
            print('Время вышло. Конец игры.')


dungeon = Dungeon('rpg.json')
dungeon.main()

# Учитывая время и опыт, не забывайте о точности вычислений!
