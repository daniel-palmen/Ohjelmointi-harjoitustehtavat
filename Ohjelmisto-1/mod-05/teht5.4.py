
n = 0
Maara  = 5
Flare = 5
Lista = []

for n in range(Maara):
    if Flare == 1:
        Kpnk = input(f'Anna {Flare}. kaupungin nimi: ')
        Lista.append(Kpnk)
    else:
        Kpnk = input(f'Anna {Flare}. kaupungin nimet: ')
        Lista.append(Kpnk)
    Flare  = Flare - 1

for nimi in Lista:
    print(nimi)