
Matikka = int(input('Anna matematiikan tulos: '))
Fysiikka = int(input('Anna fysiikan tulos: '))
Kemia = int(input('Anna kemian tulos: '))

if Matikka < 50 or Fysiikka < 50 or Kemia < 50:
    if Matikka < 50:
        print(f'Tulos Matematiikassa {Matikka} on alle 50.')
    if Fysiikka < 50:
        print(f'Tulos Fysiikassa {Fysiikka} on alle 50.')
    if Kemia < 50:
        print(f'Tulos Kemiassa {Kemia} on alle 50.')
    print('Et saa stipendiä.')
elif Matikka > 90 and Fysiikka > 90 or Kemia > 95:
    print('Saat stipendin.')
