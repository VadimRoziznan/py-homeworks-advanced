from unittest import TestCase
from test_object.task_1 import visits_list
from test_object.task_2 import check_id
from test_object.task_3 import check_queries


class TestHomeWork(TestCase):

    def test_task_1(self):
        sample = [
            {'visit1': ['Москва', 'Россия']}
        ]
        result = list(visits_list(sample)[0].values())[0][1]
        expected = 'Россия'
        self.assertEqual(result, expected)

    def test_task_2(self):
        sample = {
            'user1': [213, 213, 213, 15, 213],
            'user2': [54, 54, 119, 119, 119],
            'user3': [213, 98, 98, 35]
        }
        result = check_id(sample)
        expected = [98, 35, 213, 54, 119, 15]
        self.assertEqual(result, expected)

    def test_task_3(self):
        sample = ['смотреть сериалы онлайн']
        result = check_queries(sample)
        expected = 'Поисковых запросов из 3 слов 100.0'
        for el in result:
            self.assertEqual(el, expected)

