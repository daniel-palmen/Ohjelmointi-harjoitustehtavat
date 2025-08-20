Vuosi = int(input('Anna vuosi: '))

Jjnelja = Vuosi % 4
Jjsata = Vuosi % 100
Jjnsata = Vuosi % 400
print(f'testi{Jjnelja} {Jjsata} {Jjnsata}')

if Jjnelja != 0:
    print(f'Vuosi {Vuosi} ei ole karkausvuosi.')
elif Jjnelja == 0 and Jjsata == 0 and Jjnsata == 0:
    print(f'Vuosi {Vuosi} on karkausvuosi.')
else:
    print(f'Vuosi {Vuosi} ei ole karkausvuosi.')