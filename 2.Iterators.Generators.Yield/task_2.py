import types


def flat_generator(list_of_lists):
    main_count = 0
    auxiliary_count = 0
    while main_count <= len(list_of_lists):
        try:
            x = list_of_lists[main_count][auxiliary_count]
            auxiliary_count += 1
            yield x
        except:
            main_count += 1
            auxiliary_count = 0
            if main_count >= len(list_of_lists):
                return
            else:
                x = list_of_lists[main_count][auxiliary_count]
                auxiliary_count += 1
                yield x


def test_2():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):


        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


if __name__ == '__main__':
    test_2()