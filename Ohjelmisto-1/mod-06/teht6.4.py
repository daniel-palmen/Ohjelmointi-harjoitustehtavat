
def summain(lista):
    Summa = 0
    for i in lista:
        Summa = Summa + i
    return Summa

lista = []
print('Anna 5 lukua: ')
while len(lista) < 5:
    Luku = float(input())
    lista.append(Luku)
Summa = summain(lista)
print(f'Lukujen summa on {Summa}')