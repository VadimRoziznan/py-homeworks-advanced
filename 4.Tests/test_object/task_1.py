##Дан список с визитами по городам и странам. Напишите код, который
##возвращает отфильтрованный список geo_logs, содержащий только визиты из России."

def visits_list(list_):
    for visit in range(len(list_)-1, -1, -1):
        if 'Россия' not in list(list_[visit].values())[0]:
            list_.remove(list_[visit])
    return list_


if __name__ == '__main__':
    geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]
    print(list(visits_list(geo_logs)[0].values())[0][1])
