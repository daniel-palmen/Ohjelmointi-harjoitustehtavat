nimet = set()
nimi = str
while nimi != '':
    nimi = input('Syötä nimi (tyhjä lopettaa): ')
    if nimi == '':
        break
    elif nimi in nimet:
        print('Aiemmin syötetty nimi')
    elif nimi not in nimet:
        print('Uusi Nimi')
        nimet.add(nimi)

for i in nimet:
    print(i)