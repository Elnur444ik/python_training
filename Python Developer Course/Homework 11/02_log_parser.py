# -*- coding: utf-8 -*-

# На основе своего кода из lesson_009/02_log_parser.py напишите итератор (или генератор)
# котрый читает исходный файл events.txt и выдает число событий NOK за каждую минуту
# <время> <число повторений>
#
# пример использования:
#
# grouped_events = <создание итератора/генератора>
# for group_time, event_count in grouped_events:
#     print(f'[{group_time}] {event_count}')
#
# на консоли должно появится что-то вроде
#
# [2018-05-17 01:57] 1234

class LogWriter:

    def __init__(self, file_name):
        self.file_name = file_name
        self.log_count = ''
        self.prev_log = ''
        self.log = ' '
        self.group_time = ''
        self.event_count = 0
        self.file = ''
        self.a = True

    def __iter__(self):
        self.file = open(self.file_name, 'r', encoding='cp1251')
        return self

    def __next__(self):
        for line in self.file:
            if line:
                if 'NOK' in line:
                    self.log = line[1:17]
                else:
                    continue
                if self.prev_log == self.log:
                    self.log_count += 1
                else:
                    if self.prev_log != '':
                        self.group_time = self.prev_log
                        self.event_count = self.log_count
                        self.log_count = 1
                        self.prev_log = self.log
                        return self.group_time, self.event_count
                    else:
                        self.log_count = 1
                        self.prev_log = self.log
                        continue

        else:
            while self.a:
                self.group_time = self.prev_log
                self.event_count = self.log_count
                self.a = False
                return self.group_time, self.event_count
            else:
                raise StopIteration()




                # self.log_count = 1
                # self.prev_log = self.log
        # return group_time, event_count


grouped_events = LogWriter('events.txt')
for group_time, event_count in grouped_events:
    print(f'[{group_time}] {event_count}')
