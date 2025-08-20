Luku = 0
Min = 0
Max = 0
Check = 0
print('Palauta tyhjä lopettaa.')
while Luku != '':
    Luku = input('Anna luku: ')
    if Luku == '':
        break
    Luku = float(Luku)
    if Check == 0:
        Min = Luku
        Max = Luku
        Check = Check + 1
    if Luku < Min:
        Min = Luku
    if Luku > Max:
        Max = Luku
print(f'Suurin annettu luku on {Max} pienin annettu on {Min}')