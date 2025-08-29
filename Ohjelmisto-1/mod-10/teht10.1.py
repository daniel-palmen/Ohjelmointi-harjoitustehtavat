
class hissi:
    def __init__(self, AlinKerros, YlinKerros, NykyinenKerros):
        self.AlinKerros = AlinKerros
        self.YlinKerros = YlinKerros
        self.NykyinenKerros = NykyinenKerros
    def __str__(self):
        return f'Alin Kerros:{self.AlinKerros} YlinKerros:{self.YlinKerros} Nykyinen Kerros:{self.NykyinenKerros}'
    def siirry_kerrokseen(self, Muutos):
        if Muutos > self.NykyinenKerros:
            for i in range (self.NykyinenKerros, Muutos):
                if self.NykyinenKerros == self.YlinKerros:
                    print(f'Ylin kerros {self.YlinKerros}')
                    break
                self.kerros_ylös()
        if Muutos < self.NykyinenKerros:
            Alaspain = self.NykyinenKerros - Muutos
            for i in range (0, Alaspain):
                if self.NykyinenKerros == self.AlinKerros:
                    print(f'Alin Kerros {self.AlinKerros}')
                    break
                self.kerros_alas()
    def kerros_ylös(self):
       self.NykyinenKerros = self.NykyinenKerros + 1
       print(f'Nykyinen Kerros {self.NykyinenKerros}')
    def kerros_alas(self):
        self.NykyinenKerros = self.NykyinenKerros - 1
        print(f'Nykyinen Kerros {self.NykyinenKerros}')

Muutos = 0
print('Ohjelmisto on hissi.')
AlinKerros = int(input('Anna alin kerros: '))
YlinKerros = int(input('Anna ylin kerros: '))
Hissi = hissi(AlinKerros, YlinKerros, AlinKerros)
while Muutos != '':
    Muutos = input('Anna Haluttu kerros (tyhjä lopettaa): ')
    if Muutos == '':
        print('Kiitos ohjelman käytöstä.')
        break
    else:
        Muutos = int(Muutos)
        Hissi.siirry_kerrokseen(Muutos)
print(Hissi)