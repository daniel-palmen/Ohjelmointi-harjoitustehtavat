import requests
vastaus = requests.get('https://api.chucknorris.io/jokes/random')
data = vastaus.json()
print(f'\n{data["value"]}\n')