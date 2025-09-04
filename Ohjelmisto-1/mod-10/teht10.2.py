
class hissi:
    def __init__(self, alinKerros, ylinKerros, nykyinenKerros):
        self.alinKerros = alinKerros
        self.ylinKerros = ylinKerros
        self.nykyinenKerros = nykyinenKerros
    def __str__(self):
        return (f'Alin Kerros:{self.alinKerros} YlinKerros:{self.ylinKerros} Nykyinen Kerros:{self.nykyinenKerros}')
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

class talo:
    def __init__(self, alinKerros, ylinKerros):
        self.alinKerros = alinKerros
        self.ylinKerros = ylinKerros
        self.hissit = []
    def __str__(self):
        return (f'Alin kerros:{self.alinKerros} Ylin kerros:{self.ylinKerros} Hissit:{self.hissit}')
    def aja_hissiä (self, hissiNro, muutos):
        if muutos == self.hissit[hissiNro].nykyinenKerros:
            print(f'Hissi numero {hissiNro} on jo kerroksessa {muutos}.')
            return
        print(f'Hissi numero {hissiNro} liikkuu.')
        self.hissit[hissiNro].siirry_kerrokseen(muutos)
    def palohälytys (self):
        print(f'Palohälytys! hissit liikkuvat alimpaan kerrokseen.')
        for i in range(len(self.hissit)):
            muutos = self.hissit[i].alinKerros  #toimii myös self.alinKerros eli talon alin kerros
            self.aja_hissiä(i, muutos)

alinKerros = 0
ylinKerros = 10
hissienMaara = 3

talo1 = talo(alinKerros, ylinKerros)
for i in range(0, hissienMaara):
    i = hissi(alinKerros, ylinKerros, alinKerros)
    talo1.hissit.append(i)

hissiNro = 0
muutos = 3

talo1.aja_hissiä(hissiNro, muutos)

#Testi
for i in range(0,hissienMaara):
    print(talo1.hissit[i])

talo1.palohälytys()

#Testi
for i in range(0, hissienMaara):
    print(talo1.hissit[i])
