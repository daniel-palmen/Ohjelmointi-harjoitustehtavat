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

autojenMaara = 10
maali = 10000
lopetus = 0
lista = []
for i in range(0, autojenMaara):
    huippu = random.randint(100,200)
    rekisteri = 'ABC-{0}'.format(i + 1)
    lista.append(auto(rekisteri, huippu, 0, 0))
print(lista[0].huippunopeus)
while lopetus == 0:
    for i in range(0, autojenMaara):
        muutos = random.randint(-10, 15)
        lista[i].kiihdyta(muutos)
        lista[i].kulje(1)
        if lista[i].kuljettuMatka >= maali:
            print(f'Auto {lista[i].rekisteri} voitti kisan.')
            lopetus = 1
for i in range(0, autojenMaara):
    print(lista[i])