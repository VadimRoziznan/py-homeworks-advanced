class FlatIterator:

    def __init__(self, list_of_lists):
        self.list_of_lists = list_of_lists

    def __iter__(self):
        self.main_count = 0
        self.auxiliary_count = 0
        return self

    def __next__(self):
        try:
            x = self.list_of_lists[self.main_count][self.auxiliary_count]
            self.auxiliary_count += 1
            return x
        except:
            self.main_count += 1
            self.auxiliary_count = 0
            if self.main_count >= len(self.list_of_lists):
                raise StopIteration
            else:
                x = self.list_of_lists[self.main_count][self.auxiliary_count]
                self.auxiliary_count += 1
                return x


def test_1():
    list_of_lists_1 = [
        ["a", "b", "c"], ["d", "e", "f", "h", False], [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
        FlatIterator(list_of_lists_1),
        ["a", "b", "c", "d", "e", "f", "h", False, 1, 2, None],
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == [
        "a", "b", "c", "d", "e", "f", "h", False, 1, 2, None,
    ]


if __name__ == "__main__":
    test_1()
