
Ika = int(input('Anna ikäsi: '))

if Ika >= 18:
    print('Voit äänestää.')
else:
    Erotus = 18 - Ika
    print(f'{Erotus} vuotta ennen kuin voit äänestää.')