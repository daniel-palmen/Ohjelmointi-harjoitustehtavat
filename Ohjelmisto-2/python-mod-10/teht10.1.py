
class hissi:
    def __init__(self, alinKerros, ylinKerros, nykyinenKerros):
        self.alinKerros = alinKerros
        self.ylinKerros = ylinKerros
        self.nykyinenKerros = nykyinenKerros
    def __str__(self):
        return f'Alin Kerros:{self.alinKerros} YlinKerros:{self.ylinKerros} Nykyinen Kerros:{self.nykyinenKerros}'
    def siirry_kerrokseen(self, muutos):
        if muutos > self.nykyinenKerros:
            for i in range (self.nykyinenKerros, muutos):
                if self.nykyinenKerros == self.ylinKerros:
                    print(f'Ylin kerros {self.ylinKerros}')
                    break
                self.kerros_ylös()
        if muutos < self.nykyinenKerros:
            alaspain = self.nykyinenKerros - muutos
            for i in range (0, alaspain):
                if self.nykyinenKerros == self.alinKerros:
                    print(f'Alin Kerros {self.alinKerros}')
                    break
                self.kerros_alas()
    def kerros_ylös(self):
       self.nykyinenKerros = self.nykyinenKerros + 1
       print(f'Nykyinen Kerros {self.nykyinenKerros}')
    def kerros_alas(self):
        self.nykyinenKerros = self.nykyinenKerros - 1
        print(f'Nykyinen Kerros {self.nykyinenKerros}')

muutos = 0
print('Ohjelmisto on hissi.')
alinKerros = int(input('Anna alin kerros: '))
ylinKerros = int(input('Anna ylin kerros: '))
hissi = hissi(alinKerros, ylinKerros, alinKerros)
while muutos != '':
    muutos = input('Anna Haluttu kerros (tyhjä lopettaa): ')
    if muutos == '':
        print('Kiitos ohjelman käytöstä.')
        break
    else:
        muutos = int(muutos)
        hissi.siirry_kerrokseen(muutos)
print(hissi)