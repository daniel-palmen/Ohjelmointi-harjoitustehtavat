KOikea = 'python'
SOikea = 'rules'
i = 0
Tries = 0
while i == 0:
    Kayttaja = input('Syötä käyttäjätunnus: ')
    Salasana = input('Syötä salasana: ')
    if Kayttaja == KOikea and Salasana == SOikea:
        print('Tervetuloa')
        break
    elif Tries > 4:
        print('Pääsy evätty')
        break
    else:
        print('Virheellinen käyttäjätunnus tai salasana.\n')
        Tries = Tries + 1