vuodenajat = ('talvi','kevät','kesä','syksy')
kuukausi = int(input('Anna kuukauden numero: '))
if 1 > kuukausi or kuukausi > 12:
    print('Vuodessa on 12 kuukautta.')
    quit()
if kuukausi in (1, 2, 12):
    jarjestysnro = 0
    print('testi1')
elif kuukausi in (3, 4, 5):
    jarjestysnro = 1
    print('testi2')
elif kuukausi in (6, 7, 8):
    jarjestysnro = 2
elif kuukausi in (9, 10, 11):
    jarjestysnro = 3
vuodenaika = vuodenajat[jarjestysnro]
print(f'{kuukausi} kuukauden vuodenaika on {vuodenaika}')