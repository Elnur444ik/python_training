from io import BytesIO

import requests
from PIL import Image, ImageDraw, ImageFont

TEMPLATE_PATH = 'files\\ticket_template.png'
FONT_PATH = 'files\\Times_New_Roman.ttf'
FONT_SIZE = 20

BLACK = (0, 0, 0, 255)

NAME_OFFSET = (350, 285)
EMAIL_OFFSET = (350, 348)


def generate_ticket(name, email):
    """
    Указывает на шаблоне имя и адрес эл. почты, и сохраняет билет

    """
    base = Image.open(TEMPLATE_PATH).convert('RGBA')
    font = ImageFont.truetype(FONT_PATH, FONT_SIZE)

    draw = ImageDraw.Draw(base)
    draw.text(NAME_OFFSET, name, font=font, fill=BLACK)
    draw.text(EMAIL_OFFSET, email, font=font, fill=BLACK)

    temp_file = BytesIO()
    base.save(temp_file, 'png')
    temp_file.seek(0)

    return temp_file

