# -*- coding: utf-8 -*-

# Имеется файл events.txt вида:
#
# [2018-05-17 01:55:52.665804] NOK
# [2018-05-17 01:56:23.665804] OK
# [2018-05-17 01:56:55.665804] OK
# [2018-05-17 01:57:16.665804] NOK
# [2018-05-17 01:57:58.665804] OK
# ...
#
# Напишите программу, которая считывает файл
# и выводит число событий NOK за каждую минуту в другой файл в формате
#
# [2018-05-17 01:57] 1234
# [2018-05-17 01:58] 4321
# ...
#
# Входные параметры: файл для анализа, файл результата
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

class LogReader:

    def __init__(self, file_name):
        self.file_name = file_name
        self.log_count = ''
        self.prev_log = ''
        self.log = ' '

    def read_file(self, output_file):
        if self.file_name.endswith('.txt'):
            with open(self.file_name, 'r', encoding='cp1251') as file:
                self.file_name = file
                out_file = open(output_file, 'w')
                for line in self.file_name:
                    if 'NOK' in line:
                        self.log = line[:17] + ']'
                        self.write_file(out_file)
                out_file.close()
        else:
            print('Файл не поддерживаемого формата!')

    def write_file(self, out_file):
        if self.prev_log == self.log:
            self.log_count += 1
        else:
            if self.prev_log != '':
                log_string = self.prev_log + ' ' + str(self.log_count) + '\n'
                out_file.write(log_string)
            self.log_count = 1
            self.prev_log = self.log

    # def analys_line(self, file_name):
    #     for line in file_name:
    #         if 'NOK' in line:
    #             print('тУТ!')
    #             self.log = line[:18] + ']'
    #             print(self.log)
    #             return self.log
    #         else:
    #             print(line)

    # def out_logs(self, output_file):
    #     out_file = open(output_file, 'w')
    #     if self.prev_log == self.log:
    #         self.log_count += 1
    #     else:
    #         if self.prev_log != '':
    #             log_string = self.prev_log + ' ' + str(self.log_count)
    #             out_file.write(log_string)
    #         self.log_count = 1
    #         self.prev_log = self.log
    #         out_file.close()


log_reader = LogReader('events.txt')
log_reader.read_file(output_file='output.txt')
# log_reader.analys_line(file_name='events.txt')
# log_reader.out_logs(output_file='output.txt')






    # После выполнения первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
