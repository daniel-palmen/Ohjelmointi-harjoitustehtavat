Summa = 0
Kulutus = float(input('Anna sähkönkulutus kilowattitunteina: '))

if Kulutus < 0:
    Summa = 0
elif Kulutus <= 50:
    Summa = Kulutus * 0.1
elif Kulutus <= 200:
    Kulutus = Kulutus - 50
    Summa = 50 * 0.1
    Summa = Summa + Kulutus * 0.08
elif Kulutus > 200:
    Kulutus = Kulutus - 200
    Summa = 50 *0.1
    Summa = Summa + 150 * 0.08
    Summa = Summa + Kulutus * 0.06

print(f'Sähkön hinta on {Summa}€')