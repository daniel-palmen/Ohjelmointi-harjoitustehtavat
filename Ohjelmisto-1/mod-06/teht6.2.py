import random
def heittaja(Tahkot):
    Luku = random.randint(1,Tahkot)
    return Luku

Luku = 0
Kierros = 0
print('Ohjelma heittää noppaa kunnes tulee suurin luku.')
Tahkot = int(input('Anna nopan sivujen määrä: '))
while Luku != Tahkot:
    Luku = heittaja(Tahkot)
    Kierros = Kierros + 1
    print(f'Heiton {Kierros} luku on {Luku}')