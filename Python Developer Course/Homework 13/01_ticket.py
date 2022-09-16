# -*- coding: utf-8 -*-


# Заполнить все поля в билете на самолет.
# Создать функцию, принимающую параметры: ФИО, откуда, куда, дата вылета,
# и заполняющую ими шаблон билета Skillbox Airline.
# Шаблон взять в файле lesson_013/images/ticket_template.png
# Пример заполнения lesson_013/images/ticket_sample.png
# Подходящий шрифт искать на сайте ofont.ru


import os
from PIL import Image, ImageDraw, ImageFont, ImageColor


class TicketMaker:

    def __init__(self, fio, from_, to, date, template=None, font_path=None):
        self.fio = fio
        self.from_ = from_
        self.to = to
        self.date = date
        self.template = 'images/ticket_template.png' if template is None else template
        if font_path is None:
            self.font_path = os.path.join('ofont.ru_Onest.ttf')
        else:
            self.font_path = font_path

    def make_ticket(self, out_path=None):
        im = Image.open(self.template)

        draw = ImageDraw.Draw(im)

        font = ImageFont.truetype(self.font_path, size=15)
        date_font = ImageFont.truetype(self.font_path, size=13)

        color = ImageColor.colormap['black']

        draw.text((45, 120), self.fio, font=font, fill=color)
        draw.text((45, 190), self.from_, font=font, fill=color)
        draw.text((45, 255), self.to, font=font, fill=color)
        draw.text((285, 260), self.date, font=date_font, fill=color)

        out_path = out_path if out_path else 'SkillBox_image.png'
        im.save(out_path)
        print(f'Ticket saved as {out_path}')


if __name__ == '__main__':
    ticket = TicketMaker(fio='Фаттаев Эльнур Мирбагирович', from_='Рязань', to='Счастливая Жизнь', date='01.09.2022')
    ticket.make_ticket()

# Усложненное задание (делать по желанию).
# Написать консольный скрипт c помощью встроенного python-модуля agrparse.
# Скрипт должен принимать параметры:
#   --fio - обязательный, фамилия.
#   --from - обязательный, откуда летим.
#   --to - обязательный, куда летим.
#   --date - обязательный, когда летим.
#   --save_to - необязательный, путь для сохранения заполненнего билета.
# и заполнять билет.
