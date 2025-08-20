import random
Luku = random.randint(1,10)
Arvaus = 11
while Arvaus != Luku:
    Arvaus = int(input('Arvaa luku väliltä 1-10: '))
    if Arvaus == Luku:
        print('Oikein')
        break
    elif Arvaus <= Luku:
        print('Liian pieni arvaus')
    elif Arvaus >= Luku:
        print('Liian suuri arvaus')