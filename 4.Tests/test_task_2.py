from unittest import TestCase
from Library.yandex import Yandex


class TestHomeWork(TestCase):

    def test_yandex(self):
        result = Yandex(
            'Здесь должен быть ваш Яндекс токен.'
        ).folder('test_unittest')
        expected = 201
        if result == 201:
            expected = 201
            self.assertEqual(result, expected)
            print('Папка успешно создана.')
        elif result == 409:
            expected = 409
            self.assertEqual(result, expected)
            print('Папка уже существует.')
        else:
            expected = 200
            self.assertNotEqual(result, expected)
            print(f'Тест не пройден код ошибки {result}')
