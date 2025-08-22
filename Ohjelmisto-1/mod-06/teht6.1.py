import random
def heittaja():
    Luku = random.randint(1,6)
    return Luku

Luku = 0
Haluttu = 6
Kierros = 0
print(f'Ohjelma heittää noppaa kunnes tulee luku {Haluttu}.')
while Luku != 6:
    Luku = heittaja()
    Kierros = Kierros + 1
    print(f'Heiton {Kierros} luku on {Luku}')