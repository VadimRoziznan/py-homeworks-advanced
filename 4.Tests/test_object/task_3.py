#Дан список поисковых запросов. Получить распределение количества
#слов в них. Т.е. поисковых запросов из одного - слова 5%,
#из двух - 7%, из трех - 3% и т.д.


def check_queries(quer):
    num_list = []
    for i in range(len(quer)):
        num_list.append(len((quer[i]).split(' ')))
    for j in (set(num_list) | set(num_list)):
        p = num_list.count(j)
        yield f'Поисковых запросов из {j} слов {p * (100 / len(num_list))}'


if __name__ == '__main__':
    queries = [
        'смотреть сериалы онлайн',
        'новости спорта',
        'афиша кино',
        'курс доллара',
        'сериалы этим летом',
        'курс по питону',
        'сериалы про спорт'
    ]
    for k in check_queries(queries):
        print(k)

