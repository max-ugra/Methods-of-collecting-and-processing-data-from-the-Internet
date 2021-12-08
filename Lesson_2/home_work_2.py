import requests
import re
from pprint import pprint
from bs4 import BeautifulSoup

url = 'https://hh.ru/search/vacancy'
vacancy = 'Python'
search = 20
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'}

n_page = 0
vacancies = []
while n_page <= search - 1:
    params = {'L_is_auto_search': 'false',
              'area': '2',
              'clusters': 'true',
              'enable_snippets': 'true',
              'text': vacancy,
              'page': n_page}
    responce = requests.get(url, params=params, headers=headers)

    if responce.status_code == 200:
        dom = BeautifulSoup(responce.text, 'html.parser')
        vacancy_list = dom.find_all('div', {'class': 'vacancy-serp-item__row vacancy-serp-item__row_header'})

        for vacancy in vacancy_list:
            vacancy_data = {}
            vacancy_name = vacancy.find('a').text
            vacancy_link = vacancy.find('a')['href']
            vacancy_salary = vacancy.find('span', {'data-qa': 'vacancy-serp__vacancy-compensation'})

            if not vacancy_salary:
                salary_min = None
                salary_max = None
                salary_currency = None
            else:
                vacancy_salary = vacancy_salary.getText().replace(u'\xa0', u'')
                vacancy_salary = re.split(r'\s|-', vacancy_salary)
                if vacancy_salary[0] == 'до':
                    salary_min = None
                    salary_max = float(vacancy_salary[1])
                elif vacancy_salary[0] == 'от':
                    salary_max = None
                    salary_min = float(vacancy_salary[1])
                else:
                    salary_max = float(vacancy_salary[1])
                    salary_min = float(vacancy_salary[0])

                salary_currency = vacancy_salary[-1]

            vacancy_data['name'] = vacancy_name
            vacancy_data['vacancy_link'] = vacancy_link
            vacancy_data['salary_min'] = salary_min
            vacancy_data['salary_max'] = salary_max
            vacancy_data['currency'] = salary_currency
            vacancies.append(vacancy_data)

    n_page += 1
pprint(vacancies)
