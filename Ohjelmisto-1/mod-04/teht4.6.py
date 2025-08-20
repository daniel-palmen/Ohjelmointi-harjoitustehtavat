import random
i = 0
n = 0
print('Ohjelma laskee piin likiarvon')
N = int(input('Anna arvottavien pisteiden määrä: '))
while i <= N:
    x = random.uniform(-1,1)
    y =random.uniform (-1,1)
    Lasku = x**2 + y**2
    if Lasku < 1:
        n = n + 1
    i = i + 1
pii = 4 * n / N
print(f'Likiarvo in {pii}')