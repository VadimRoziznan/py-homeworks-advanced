import os
import datetime
from functools import wraps


def logger(path):

    def __logger(old_function):
        @wraps(old_function)
        def new_function(*args, **kwargs):
            result = old_function(*args, **kwargs)
            date = datetime.datetime.now()
            value = f"{date, old_function.__name__, args, kwargs, result}"
            if result:
                full_path = os.path.join(os.getcwd(), "logs", path)
                with open(full_path, "a") as log_file:
                    log_file.write(value)
            return result
        return new_function

    return __logger


def test_2():
    paths = ('log_1.log', 'log_2.log', 'log_3.log')

    for path in paths:
        full_path = os.path.join(os.getcwd(), "logs", path)
        if os.path.exists(full_path):
            os.remove(full_path)

        @logger(path)
        def hello_world():
            return 'Hello World'

        @logger(path)
        def summator(a, b=0):
            return a + b

        @logger(path)
        def div(a, b):
            return a / b


        assert 'Hello World' == hello_world(), "Функция возвращает 'Hello World'"
        result = summator(2, 2)
        assert isinstance(result, int), 'Должно вернуться целое число'
        assert result == 4, '2 + 2 = 4'
        result = div(6, 2)
        assert result == 3, '6 / 2 = 3'
        summator(4.3, b=2.2)

    for path in paths:

        full_path = os.path.join(os.getcwd(), "logs", path)

        assert os.path.exists(full_path), f'файл {path} должен существовать'

        with open(full_path) as log_file:
            log_file_content = log_file.read()

        assert 'summator' in log_file_content, 'должно записаться имя функции'

        for item in (4.3, 2.2, 6.5):
            assert str(
                item) in log_file_content, f'{item} должен быть записан в файл'


if __name__ == '__main__':
    test_2()