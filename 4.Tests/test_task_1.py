from unittest import TestCase
from test_object.task_1 import visits_list

class TestHomeWork(TestCase):
    def test_task_1(self):
        x = [
        {'visit10': ['Архангельск', 'Россия']}
            ]
        result = list(visits_list(x)[0].values())[0][1]
        expected = 'Россия'
        self.assertEqual(result, expected)

