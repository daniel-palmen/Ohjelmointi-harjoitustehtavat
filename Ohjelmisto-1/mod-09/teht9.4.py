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

AutojenMaara = 10
Maali = 10000
Lopetus = 0
Lista = []
for i in range(0, AutojenMaara):
    Huippu = random.randint(100,200)
    rekisteri = 'ABC-{0}'.format(i + 1)
    Lista.append(auto(rekisteri, Huippu, 0, 0))
print(Lista[0].huippunopeus)
while Lopetus == 0:
    for i in range(0, AutojenMaara):
        muutos = random.randint(-10, 15)
        Lista[i].kiihdyta(muutos)
        Lista[i].kulje(1)
        if Lista[i].kuljettuMatka >= Maali:
            print(f'Auto {Lista[i].rekisteri} voitti kisan.')
            Lopetus = 1
for i in range(0, AutojenMaara):
    print(Lista[i])