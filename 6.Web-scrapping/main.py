import requests
from fake_headers import Headers
from bs4 import BeautifulSoup
import json

HOST = 'https://spb.hh.ru'
MAIN = f'{HOST}/search/vacancy?area=1&area=2&ored_clusters=true&text=' \
       f'python&search_period=1'


def get_headers():
    return Headers(browser='firefox', os='win').generate()


main_page = requests.get(MAIN, headers=get_headers()).text

bs = BeautifulSoup(main_page, features='lxml')

vacancy_list = bs.find(
    class_='vacancy-serp-content'
).find_all(
    class_='serp-item'
)

parsed_data = []

for vacancy in vacancy_list:
    job_name = vacancy.find('h3').find('span').text
    link = vacancy.find('a', class_='serp-item__title')['href']
    try:
        salary_fork = vacancy.find('span', class_='bloko-header-section-3').text
    except:
        salary_fork = 'Уровень заработной платы не указан.'
    company = vacancy.find(class_='bloko-text').text
    city = vacancy.find(
        class_='vacancy-serp-item__info'
    ).find_all(
        class_="bloko-text"
    )[1].text
    full_vacancy_html = requests.get(link, headers=get_headers()).text
    full_vacancy_bs = BeautifulSoup(full_vacancy_html, features='lxml')
    text = full_vacancy_bs.find(class_='g-user-content').text
    if "Django" and "Flask" in text:
        parsed_data.append({
            'job_name': job_name,
            'salary_fork': salary_fork,
            'company': company,
            'city': city,
            'link': link,
            'description': text
        })

with open('report.json', 'w') as rep:
    json.dump(parsed_data,  rep, indent=2)
