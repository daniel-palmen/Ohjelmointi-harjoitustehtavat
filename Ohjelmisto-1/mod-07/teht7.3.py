def valikko():
    print('valikko:')
    print('1 Syötä uusi lentoasema')
    print('2 Hae jo syötetty lentoasema')
    print('0 Lopeta')
    valinta = int(input('Anna valinta: '))
    return valinta
w = 0
print('Ohjelmassa voit tallentaa ja hakea lentoaseman tietoja.')
Sanakirja = {}
while w == 0:
    Valinta = valikko()
    if Valinta == 0:
        print('Kiitos ohjelman käytöstä.')
        break
    if Valinta == 1:
        Icao = input('Anna syötettävän lentoaseman ICAO-koodi: ')
        Nimi = input('Anna syötettävän lentoaseman nimi: ')
        Sanakirja[Icao] = Nimi
    if Valinta == 2:
        Icao = input('Anna haettavan lentoaseman ICAO-koodi: ')
        if Icao in Sanakirja:
            print(f'{Icao} lentokentän nimi on {Sanakirja[Icao]}.')