# -*- coding: utf-8 -*-

# Есть файл с протоколом регистраций пользователей на сайте - registrations.txt
# Каждая строка содержит: ИМЯ ЕМЕЙЛ ВОЗРАСТ, разделенные пробелами
# Например:
# Василий test@test.ru 27
#
# Надо проверить данные из файла, для каждой строки:
# - присутсвуют все три поля
# - поле имени содержит только буквы
# - поле емейл содержит @ и .
# - поле возраст является числом от 10 до 99
#
# В результате проверки нужно сформировать два файла
# - registrations_good.log для правильных данных, записывать строки как есть
# - registrations_bad.log для ошибочных, записывать строку и вид ошибки.
#
# Для валидации строки данных написать метод, который может выкидывать исключения:
# - НЕ присутсвуют все три поля: ValueError
# - поле имени содержит НЕ только буквы: NotNameError (кастомное исключение)
# - поле емейл НЕ содержит @ и .(точку): NotEmailError (кастомное исключение)
# - поле возраст НЕ является числом от 10 до 99: ValueError
# Вызов метода обернуть в try-except.

class NotNameError(Exception):
    pass


class NotEmailError(Exception):
    pass


def check(line):
    name, mail, age = line.split(' ')
    for symbol in name:
        if symbol.isalpha() is False:
            raise NotNameError()
    if '@' not in mail or '.' not in mail:
        raise NotEmailError()
    if not 10 <= int(age) <= 99:
        raise ValueError


with open('registrations.txt', 'r', encoding='utf8') as file:
    bad_log = open('registrations_bad.log', 'w')
    good_log = open('registrations_good.log', 'w')
    for line in file:
        try:
            check(line)
        except ValueError as exc:
            bad_log.write(line)
            if exc.args:
                print(f'Не хватает данных в строке: {line}')
            else:
                print(f'Значение возраста выходит за пределы: {line}')
        except NotEmailError:
            bad_log.write(line)
            print(f'Не корректно введён E-Mail в строке: {line}')
        except NotNameError:
            bad_log.write(line)
            print(f'Имя введено некорректно на строке: {line}')
        else:
            good_log.write(line)
    good_log.close()
    bad_log.close()




        # finally:
        #     good_log.close()
        #     bad_log.close()

# good_log = open('registrations_good.log', 'w')
# bad_log = open('registrations_bad.log', 'w')
#
# good_log.close()
# bad_log.close()