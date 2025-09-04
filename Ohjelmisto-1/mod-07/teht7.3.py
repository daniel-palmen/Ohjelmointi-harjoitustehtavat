def valikko():
    print('valikko:')
    print('1 Syötä uusi lentoasema')
    print('2 Hae jo syötetty lentoasema')
    print('0 Lopeta')
    valinta = int(input('Anna valinta: '))
    return valinta
w = 0
print('Ohjelmassa voit tallentaa ja hakea lentoaseman tietoja.')
sanakirja = {}
while w == 0:
    valinta = valikko()
    if valinta == 0:
        print('Kiitos ohjelman käytöstä.')
        break
    if valinta == 1:
        icao = input('Anna syötettävän lentoaseman ICAO-koodi: ')
        nimi = input('Anna syötettävän lentoaseman nimi: ')
        sanakirja[icao] = nimi
    if valinta == 2:
        icao = input('Anna haettavan lentoaseman ICAO-koodi: ')
        if icao in sanakirja:
            print(f'{icao} lentokentän nimi on {sanakirja[icao]}.')