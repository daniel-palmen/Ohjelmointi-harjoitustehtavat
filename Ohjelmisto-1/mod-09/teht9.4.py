import random
class auto:
    def __init__(self, rekisteri, huippunopeus, tamanhetkinenNopeus, kuljettuMatka):
        self.rekisteri = rekisteri
        self.huippunopeus = huippunopeus
        self.tamanhetkinenNopeus = tamanhetkinenNopeus
        self.kuljettuMatka = kuljettuMatka
    def __str__(self):
        return f'{self.rekisteri} {self.huippunopeus}km/h {self.tamanhetkinenNopeus}km/h {self.kuljettuMatka}km'
    def kiihdyta(self, muutos):
        self.tamanhetkinenNopeus = self.tamanhetkinenNopeus + muutos
        if self.tamanhetkinenNopeus > self.huippunopeus:
            self.tamanhetkinenNopeus = self.huippunopeus
        if self.tamanhetkinenNopeus < 0:
            self.tamanhetkinenNopeus = 0
    def kulje(self, aika):
        kuljettuMatka = self.tamanhetkinenNopeus * aika
        self.kuljettuMatka = self.kuljettuMatka + kuljettuMatka

AutojenMaara = 11
Lopetus = 0
Directory = {}
for i in range(1, AutojenMaara):
    Huippu = random.randint(100,200)
    rekisteri = 'ABC-{0}'.format(i)
    Directory['Auto{0}'.format(i)] = auto(rekisteri, Huippu, 0 , 0)
print(Directory['Auto1'])
print(Directory['Auto2'])
while Lopetus == 0:
    for i in range(1, AutojenMaara):
        muutos = random.randint(-10, 15)
        Auto1.kiihdyta(muutos)
        print(Directory['Auto1'])
        Lopetus = 1