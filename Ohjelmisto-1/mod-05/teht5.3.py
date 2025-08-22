
Luku = int(input('Anna kokonaisluku: '))
x = range(Luku)
Testi = 0
n = 0

for n in x:
    n = n + 1
    print(n)
    Jj = Luku % n
    if Jj == 0:
        Testi = Testi + 1

if Testi == 2:
    print(f'Luku {Luku} on alkuluku.')
else:
    print(f'Luku {Luku} ei ole alkuluku.')