from collections.abc import Iterable

list_of_lists_2 = [
    [['a'], ['b', 'c']],
    ['d', 'e', [['f'], 'h'], False],
    [1, 2, None, [[[[['!']]]]], []]
]
c = ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


def f(l):
    for el in l:
        if isinstance(el, Iterable) and not isinstance(el, (str, bytes)):
            yield from f(el)
        else:
            yield el

print(list(f(list_of_lists_2)))

