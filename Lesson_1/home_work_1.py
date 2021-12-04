#1. Посмотреть документацию к API GitHub, разобраться как вывести список
# репозиториев для конкретного пользователя, сохранить JSON-вывод в файле *.json.

import requests
import json

url = 'https://api.github.com'
user = 'max-ugra'

response = requests.get(f'{url}/users/{user}/repos')
with open('data.json', 'w') as f:
    json.dump(response.json(), f)

    for i in response.json():
        print(i['name'])


#2. Изучить список открытых API (https://www.programmableweb.com/category/all/apis).
# Найти среди них любое, требующее авторизацию (любого типа). Выполнить запросы к нему,
# пройдя авторизацию. Ответ сервера записать в файл.
# Если нет желания заморачиваться с поиском, возьмите API вконтакте (https://vk.com/dev/first_guide).
# Сделайте запрос, чтобы получить список всех сообществ на которые вы подписаны.

ap_key = '6ad65bd365334339b1d190955211611'
city = 'Moscow'
url = f'https://api.weatherapi.com/v1/current.json'
params = {'key': ap_key,
          'q': city}

response = requests.get(url, params=params)
j_data = response.json()
print(f"В {j_data.get('location').get('name')} температура {j_data.get('current').get('temp_c')} градусов Цельсия")

with open('weather.json', 'w') as f:
    json.dump(response.json(), f)
