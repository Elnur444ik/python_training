# -*- coding: utf-8 -*-

import os
import shutil
import time


# Нужно написать скрипт для упорядочивания фотографий (вообще любых файлов)
# Скрипт должен разложить файлы из одной папки по годам и месяцам в другую.
# Например, так:
#   исходная папка
#       icons/cat.jpg
#       icons/man.jpg
#       icons/new_year_01.jpg
#   результирующая папка
#       icons_by_year/2018/05/cat.jpg
#       icons_by_year/2018/05/man.jpg
#       icons_by_year/2017/12/new_year_01.jpg
#
# Входные параметры основной функции: папка для сканирования, целевая папка.
# Имена файлов в процессе работы скрипта не менять, год и месяц взять из времени создания файла.
# Обработчик файлов делать в обьектном стиле - на классах.
#
# Файлы для работы взять из архива icons.zip - раззиповать проводником в папку icons перед написанием кода.
# Имя целевой папки - icons_by_year (тогда она не попадет в коммит)
#
# Пригодятся функции:
#   os.walk
#   os.path.dirname
#   os.path.join
#   os.path.normpath
#   os.path.getmtime
#   time.gmtime
#   os.makedirs
#   shutil.copy2
#
# Чтение документации/гугла по функциям - приветствуется. Как и поиск альтернативных вариантов :)
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

class Sorter:

    def __init__(self, path, new_directory):
        self.path = path
        self.new_directory = new_directory
        self.file_path = None
        self.file_time = None
        self.year = None
        self.mounth = None
        self.new_path = None

    def walk_through_directories(self):
        self.path = os.path.normpath(self.path)
        os.walk(self.path)
        for dirpath, dirnames, filenames in os.walk(self.path):
            for file in filenames:
                self.method_name(dirpath, file)

    def method_name(self, dirpath, file):
        self.file_path = os.path.join(dirpath, file)
        self.file_time = os.path.getmtime(self.file_path)
        self.file_time = time.gmtime(self.file_time)
        self.year = str(self.file_time[0])
        self.mounth = str(self.file_time[1])
        if len(self.mounth) == 1:
            self.mounth = '0' + self.mounth
        self.sorting_in_new_path()

    def sorting_in_new_path(self):
        self.new_path = os.path.dirname(self.path)
        self.new_path = os.path.join(self.new_path, self.new_directory, self.year, self.mounth)
        os.makedirs(self.new_path, exist_ok=True)
        shutil.copy2(self.file_path, self.new_path)


directory = Sorter('C:\\Users\\1\\Desktop\\Программирование\\Python\\Homework 9\\icons', 'icons_by_year')
directory.walk_through_directories()

# Усложненное задание (делать по желанию)
# Нужно обрабатывать zip-файл, содержащий фотографии, без предварительного извлечения файлов в папку.
# Основная функция должна брать параметром имя zip-файла и имя целевой папки.
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
