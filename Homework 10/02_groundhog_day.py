# -*- coding: utf-8 -*-

# День сурка
#
# Напишите функцию one_day() которая возвращает количество кармы от 1 до 7
# и может выкидывать исключения:
# - IamGodError
# - DrunkError
# - CarCrashError
# - GluttonyError
# - DepressionError
# - SuicideError
# Одно из этих исключений выбрасывается с вероятностью 1 к 13 каждый день
#
# Функцию оберните в бесконечный цикл, выход из которого возможен только при накоплении
# кармы до уровня ENLIGHTENMENT_CARMA_LEVEL. Исключения обработать и записать в лог.
# При создании собственных исключений максимально использовать функциональность
# базовых встроенных исключений.
from random import randint


class IamGodError(Exception):
    pass


class DrunkError(Exception):
    pass


class CarCrashError(Exception):
    pass


class GluttonyError(Exception):
    pass


class DepressionError(Exception):
    pass


class SuicideError(Exception):
    pass


class GroundhogDay:

    def __init__(self):
        self.days_to_exit = 0
        self.carma_level = 0
        self.day_carma = 0

    def one_day(self):
        while self.carma_level < ENLIGHTENMENT_CARMA_LEVEL:
            dice = randint(1, 13)
            if dice == 13:
                random_exception = randint(1, 6)
                try:
                    if random_exception == 1:
                        raise IamGodError()
                    elif random_exception == 2:
                        raise DrunkError()
                    elif random_exception == 3:
                        raise CarCrashError()
                    elif random_exception == 4:
                        raise GluttonyError()
                    elif random_exception == 5:
                        raise DepressionError()
                    else:
                        raise SuicideError()
                except IamGodError:
                    print('Герой считает себя Богом! Ты сильно ошибаешься....')
                except DrunkError:
                    print('Герой напился до смерти.... Алкоголь - это не решение проблем!')
                except CarCrashError:
                    print('Герой разбился на машине... Не стоит нарушать ПДД!!!')
                except GluttonyError:
                    print('Герой объелся до смерти.... Это один из сертных грехов!!!')
                except DepressionError:
                    print('Герой умер от депрессии.... Нельзя столько переживать из-за пустяков')
                except SuicideError:
                    print('Герой совершил суицид.... Ну зачем?!')
            else:
                self.day_carma = randint(1, 7)
                self.days_to_exit += 1
                self.carma_level += self.day_carma
                print(f'Герой прожил день без проишествий и заработал {self.day_carma} кармы!!!')

        print(f'Герой прервал день сурка за {self.days_to_exit} дней! Капитальный красавчик!!!')


ENLIGHTENMENT_CARMA_LEVEL = 777

groundhog = GroundhogDay()
groundhog.one_day()

# https://goo.gl/JnsDqu
