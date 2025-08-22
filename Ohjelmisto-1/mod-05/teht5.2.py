Luku = 0
i = 0
Lista = []
while i == 0:
    Luku = input('Anna lukuja, tyhjä lopettaa: ')
    if Luku == '':
        break
    Lista.append(Luku)
Lista.sort(reverse=True)
print(f'Listan viisi suurinta lukua')
print(Lista[0:5])