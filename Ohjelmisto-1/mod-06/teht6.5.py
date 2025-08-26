def muunnin(Lista):
    Parilliset = []
    for i in Lista:
        if i % 2 == 0:
            Parilliset.append(i)
    return Parilliset

Lista = []
print('Anna 5 lukua: ')
while len(Lista) < 5:
    Luku = float(input())
    Lista.append(Luku)
if len(Lista) == 5:
    Parilliset = muunnin(Lista)
    print(f'{Lista} Annetut luvut.')
    print(f'{Parilliset} Parilliset luvut.')