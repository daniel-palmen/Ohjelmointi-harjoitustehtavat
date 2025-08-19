print('Ohjelma kysyy kolme kokonaislukua.')
luku1 = int(input('Anna ensimmäinen luku: '))
luku2 = int(input('Anna toinen luku: '))
luku3 = int(input('Anna kolmas luku: '))

Summa = luku1+luku2+luku3
Tulo = luku1*luku2*luku3
KArvo = Summa/3

print(f'Lukujen Summa on {Summa}, tulo on {Tulo} ja keskiarvo on {KArvo:.2f}')