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
        {'visit10': ['Архангельск', 'Россия']}
    ]
    print(list(visits_list(geo_logs)[0].values())[0][1])
