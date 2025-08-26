Vuodenajat = ('talvi','kevät','kesä','syksy')
Kuukausi = int(input('Anna kuukauden numero: '))
if 1 > Kuukausi or Kuukausi > 12:
    print('Vuodessa on 12 kuukautta.')
    quit()
if Kuukausi in (1, 2, 12):
    Jarjestysnro = 0
    print('testi1')
elif Kuukausi in (3, 4, 5):
    Jarjestysnro = 1
    print('testi2')
elif Kuukausi in (6, 7, 8):
    Jarjestysnro = 2
elif Kuukausi in (9, 10, 11):
    Jarjestysnro = 3
Vuodenaika = Vuodenajat[Jarjestysnro]
print(f'{Kuukausi} kuukauden vuodenaika on {Vuodenaika}')