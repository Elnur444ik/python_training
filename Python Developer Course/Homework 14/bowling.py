def get_score(game_result):
    if not 10 <= len(game_result) < 20:
        raise ValueError('Длина результата не соответствует диапазону корректного значения!')
    elif game_result[0] == '/':
        raise ValueError('Результат не может начинаться со spare!')

    frame_count = 0
    half_frame_count = 0
    result = 0
    index = -1

    for symbol in game_result:
        if symbol == 'X':
            frame_count += 1
        else:
            half_frame_count += 1

    if (half_frame_count % 2) != 0:
        raise ValueError('Результат введен не корректно: есть неполные фреймы')
    elif frame_count + (half_frame_count / 2) != 10:
        raise ValueError('Результат введен некорректно: количество фреймов должно быть равно 10')

    for symbol in game_result:
        index += 1
        if symbol == 'X':
            result += 20
        elif symbol == '/':
            result += 15
            result -= int(game_result[index - 1])
        elif symbol == '-':
            continue
        elif symbol.isnumeric():
            result += int(symbol)
        else:
            raise ValueError('Результат введен некорректно: использованы некорректные символы')

    frame_index = -1

    for frame_symbol in game_result:
        frame_check = 0
        frame_index += 1
        if frame_index != 0 and frame_index % 2 != 0:
            if frame_symbol.isnumeric():
                if game_result[frame_index - 1].isnumeric():
                    frame_check = int(game_result[frame_index - 1]) + int(frame_symbol)
                else:
                    continue
            else:
                continue
        if frame_check >= 10:
            raise ValueError('Результат введен некорректно: числовые значения одного фрейма не могут быть больше 9')
    return result

#get_score('88XXXXXXX--X')
