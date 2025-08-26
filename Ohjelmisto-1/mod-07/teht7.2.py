Nimet = set()
Nimi = str
while Nimi != '':
    Nimi = input('Syötä nimi (tyhjä lopettaa): ')
    if Nimi == '':
        break
    elif Nimi in Nimet:
        print('Aiemmin syötetty nimi')
    elif Nimi not in Nimet:
        print('Uusi Nimi')
        Nimet.add(Nimi)

for i in Nimet:
    print(i)