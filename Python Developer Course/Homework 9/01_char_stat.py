# -*- coding: utf-8 -*-

# Подсчитать статистику по буквам в романе Война и Мир.
# Входные параметры: файл для сканирования
# Статистику считать только для букв алфавита (см функцию .isalpha() для строк)
#
# Вывести на консоль упорядоченную статистику в виде
# +---------+----------+
# |  буква  | частота  |
# +---------+----------+
# |    А    |   77777  |
# |    Б    |   55555  |
# |   ...   |   .....  |
# |    a    |   33333  |
# |    б    |   11111  |
# |   ...   |   .....  |
# +---------+----------+
# |  итого  | 9999999  |
# +---------+----------+
#
# Упорядочивание по частоте - по убыванию. Ширину таблицы подберите по своему вкусу
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.
import zipfile


class Counterer:

    def __init__(self, file_name):
        self.file_name = file_name
        self.stat = {}

    def unzip(self):
        zfile = zipfile.ZipFile(self.file_name, 'r')
        for file in zfile.namelist():
            zfile.extract(file)
        self.file_name = file

    def collect(self):
        if self.file_name.endswith('.zip'):
            self.unzip()
        with open(self.file_name, 'r', encoding='cp1251') as file:
            for line in file:
                for char in line:
                    if char.isalpha():
                        if char in self.stat:
                            self.stat[char] += 1
                        else:
                            self.stat[char] = 1

    def printer(self):
        printed_list = list(self.stat.items())
        # printed_list.sort(key=lambda x: x[1])              # - по частоте по возрастанию
        printed_list.sort(key=lambda x: x[1], reverse=True)  # - по частоте по убыванию
        # printed_list.sort()                                # - по алфавиту по возрастанию
        # printed_list.sort(reverse=True)                    # - по алфавиту по убыванию
        print('+----------+----------+')
        print('|{symbol:^10}|{sequence:^10}|'.format(symbol='Буква', sequence='Частота'))
        print('+----------+----------+')
        all_count = 0
        for tuple_char in printed_list:
            print('|{symbol:^10}|{sequence:^10}|'.format(symbol=tuple_char[0], sequence=tuple_char[1]))
            all_count += int(tuple_char[1])
            print('+----------+----------+')
        print('|{symbol:^10}|{sequence:^10}|'.format(symbol='Итого', sequence=all_count))
        print('+----------+----------+')


counter = Counterer('voyna-i-mir.txt')
counter.collect()
counter.printer()

# После выполнения первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
