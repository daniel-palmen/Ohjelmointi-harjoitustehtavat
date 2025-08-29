
class hissi:
    def __init__(self, AlinKerros, YlinKerros, NykyinenKerros):
        self.AlinKerros = AlinKerros
        self.YlinKerros = YlinKerros
        self.NykyinenKerros = NykyinenKerros
    def __str__(self):
        return (f'Alin Kerros:{self.AlinKerros} YlinKerros:{self.YlinKerros} Nykyinen Kerros:{self.NykyinenKerros}')
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
class talo:
    def __init__(self, AlinKerros, YlinKerros, Hissit):
        self.AlinKerros = AlinKerros
        self.YlinKerros = YlinKerros
        self.Hissit = []
    def __str__(self):
        return (f'Alin kerros:{self.AlinKerros} Ylin kerros:{self.YlinKerros} Hissit:{self.Hissit}')
    def aja_hissiä (self, HissiNro, Muutos):
        self.Hissit[HissiNro].siirry_kerrokseen(Muutos)
    def palohälytys (self):
        for i in self.Hissit:
            while self.Hissit[i].NykyinenKerros != self.AlinKerros: #EI TOIMI
                Muutos = -10
                Muutos = Muutos - 10
                self.aja_hissiä(i, Muutos)

AlinKerros = 0
YlinKerros = 10
HissienMaara = 3

Talo1 = talo(AlinKerros, YlinKerros,0)
for i in range(0, HissienMaara):
    i = hissi(AlinKerros, YlinKerros, 0)
    Talo1.Hissit.append(i)

HissiNro = 0
Muutos = 3

Talo1.aja_hissiä(HissiNro, Muutos)

#Testi
for i in range(0,HissienMaara):
    print(Talo1.Hissit[i])

Talo1.palohälytys()

for i in range(0, HissienMaara):
    print(Talo1.Hissit[i])