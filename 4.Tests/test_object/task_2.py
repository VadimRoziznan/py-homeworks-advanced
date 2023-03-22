##Выведите на экран все уникальные гео-ID из значений словаря ids.
##Т.е. список вида [213, 15, 54, 119, 98, 35]

def check_id(ids_):
    a = set([])
    for user, value in ids_.items():
        a = a | set(value)
    return list(a)


if __name__ == '__main__':
    ids = {'user1': [213, 213, 213, 15, 213],
           'user2': [54, 54, 119, 119, 119],
           'user3': [213, 98, 98, 35]}
    print(check_id(ids))
