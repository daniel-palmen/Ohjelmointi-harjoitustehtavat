import math
def laskin(Halkaisija, Hinta):
    Halkaisija = Halkaisija / 100
    Ala = math.pi * (Halkaisija / 2) ** 2
    Arvo = Hinta / Ala
    return Arvo

Halkaisija = float(input('Anna ensimmäisen pitsan halkaisija sentteinä: '))
Hinta = float(input('Anna ensimmäisen pitsan hinta: '))
EkaPitsa = laskin(Halkaisija, Hinta)

Halkaisija = float(input('Anna toisen pitsan halkaisija sentteinä: '))
Hinta = float(input('Anna toisen pitsan hinta: '))
TokaPitsa = laskin(Halkaisija, Hinta)

if EkaPitsa < TokaPitsa:
    print('Ensimmäinen pitsa antaa paremman vastineen rahalle.')
elif EkaPitsa > TokaPitsa:
    print('Toinen pitsa antaa paremman vastineen rahalle.')
elif EkaPitsa == TokaPitsa:
    print('Pitsat antavat saman vastineen rahalle.')