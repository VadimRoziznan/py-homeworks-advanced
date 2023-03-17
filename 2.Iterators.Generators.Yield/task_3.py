from collections.abc import Iterable


class FlatIterator:

    count = -1

    def __init__(self, list_of_list):

        self.list_of_list = list_of_list


    def __iter__(self):
        self.main_count = 0
        return self

    def __next__(self):
        try:
            x = self.list_of_list[self.main_count]
            self.main_count += 1
            return x
        except:
                raise StopIteration

    @staticmethod
    def re_formate(list_):
        for el in list_:
            if isinstance(el, Iterable) and not isinstance(el, (str, bytes)):
                yield from FlatIterator.re_formate(el)
            else:
                yield el


def test_3(list_1):
    for flat_iterator_item, check_item in zip(
           FlatIterator(list(FlatIterator.re_formate(list_1))),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item
        
    assert list(FlatIterator.re_formate(list_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    test_3(list_of_lists_2)
