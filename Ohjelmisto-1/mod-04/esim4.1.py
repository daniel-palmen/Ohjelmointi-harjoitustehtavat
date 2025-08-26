Luku = int(input('Anna positiivinen kokonaisluku: '))
i = 0
if Luku > 0:
    while i != Luku:
        if i % 2 == 0:
            print(i)
        i = i + 1
else:
    print('Virhe! Luku on 0 tai negatiivinen.')