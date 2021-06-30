import requests
import json


def weather_in_city():
    appid = '3e4198df3bd08580013f914196a556aa'
    service = 'https://samples.openweathermap.org/data/2.5/weather'
    city = input("Введите город: ")
    r = requests.get(f'{service}?q={city},uk&appid={appid}')
    data = json.loads(r.text)
    return f"В городе {data['name']} {data['main']['temp']} градусов по Кельвину"


print(weather_in_city())
