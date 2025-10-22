import requests
API = 'c89244149d1a17200e151b95a7f009e2'
kaupunki = input('Anna kaupunki: ')
haku = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={kaupunki}&units=metric&appid={API}')
data = haku.json()
description = data['weather'][0]['description']
temperature = data['main']['temp']
print(f'{description} \nTemperature: {temperature}C')