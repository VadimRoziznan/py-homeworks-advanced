boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']

if len(boys) == len(girls):
    boys.sort()
    girls.sort()
    for el in zip(boys, girls):
        print(','.join(el))
else:
    print('Дополните список, кто-то может остаться без пары.')