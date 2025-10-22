import requests
API = 'c89244149d1a17200e151b95a7f009e2'
kaupunki = 'London'
haku = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={kaupunki}&limit=1&appid={API}')
data = haku.json()
lat = data[0]["lat"]
lon = data[0]["lon"]
haku = requests.get(f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&units=metric&appid={API}')
data = haku.json()
description = data['weather'][0]['description']
temperature = data['main']['temp']
print(f'{description} Temperature: {temperature}')