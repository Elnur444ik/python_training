import unittest

from bowling import get_score


class BowlingTest(unittest.TestCase):

    def test_normal(self):
        result = get_score('18254/8123432/X1/14')
        self.assertEqual(result, 107)

    def test_low_frame(self):
        with self.assertRaises(ValueError) as exc:
            get_score('54X35325454')
        the_exception = exc.exception
        self.assertEqual(*the_exception.args,
                         'Результат введен некорректно: количество фреймов должно быть равно 10')

    def test_many_frame(self):
        with self.assertRaises(ValueError) as exc:
            get_score('XXX34125421--XX--')
        the_exception = exc.exception
        self.assertEqual(*the_exception.args,
                         'Результат введен некорректно: количество фреймов должно быть равно 10')

    def test_first_spare(self):
        with self.assertRaises(ValueError) as exc:
            get_score('/556XXXXXXX')
        the_exception = exc.exception
        self.assertEqual(*the_exception.args,
                         'Результат не может начинаться со spare!')

    def test_short_result(self):
        with self.assertRaises(ValueError) as exc:
            get_score('XXXX')
        the_exception = exc.exception
        self.assertEqual(*the_exception.args,
                         'Длина результата не соответствует диапазону корректного значения!')

    def test_Long_result(self):
        with self.assertRaises(ValueError) as exc:
            get_score('XXXXX-XXXX-XXXXXXXXXXXX-XXX')
        the_exception = exc.exception
        self.assertEqual(*the_exception.args,
                         'Длина результата не соответствует диапазону корректного значения!')

    def test_incomplete_frames(self):
        with self.assertRaises(ValueError) as exc:
            get_score('4/XXXXXXXXX3')
        the_exception = exc.exception
        self.assertEqual(*the_exception.args,
                         'Результат введен не корректно: есть неполные фреймы')

    def test_incorrect_value(self):
        with self.assertRaises(ValueError) as exc:
            get_score('445235XXXXXXa4')
        the_exception = exc.exception
        self.assertEqual(*the_exception.args,
                         'Результат введен некорректно: использованы некорректные символы')

    def test_incorrect_frame(self):
        with self.assertRaises(ValueError) as exc:
            get_score('XXXXXX55X--X')
        the_exception = exc.exception
        self.assertEqual(*the_exception.args,
                         'Результат введен некорректно: числовые значения одного фрейма не могут быть больше 9')


if __name__ == '__main__':
    unittest.main()
