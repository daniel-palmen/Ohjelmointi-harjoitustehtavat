import random

class Auto:
    def __init__(self, rekisteri, huippunopeus, tamanhetkinenNopeus, kuljettuMatka):
        self.rekisteri = rekisteri
        self.huippunopeus = huippunopeus
        self.tamanhetkinenNopeus = tamanhetkinenNopeus
        self.kuljettuMatka = kuljettuMatka
    def kiihdyta(self, muutos):
        self.tamanhetkinenNopeus = self.tamanhetkinenNopeus + muutos
        if self.tamanhetkinenNopeus > self.huippunopeus:
            self.tamanhetkinenNopeus = self.huippunopeus
        if self.tamanhetkinenNopeus < 0:
            self.tamanhetkinenNopeus = 0
    def kulje(self, aika):
        kuljettuMatka = self.tamanhetkinenNopeus * aika
        self.kuljettuMatka = self.kuljettuMatka + kuljettuMatka

class SahkoAuto(Auto):
    def __init__(self, rekisteri, huippunopeus, tamanhetkinenNopeus, kuljettuMatka, kapasiteetti):
        self.kapasiteetti = kapasiteetti
        super().__init__(rekisteri, huippunopeus, tamanhetkinenNopeus, kuljettuMatka)
    def tulosta_tiedot(self):
        print(f'Rekisteri: {self.rekisteri} kuljettu matka: {self.kuljettuMatka:.0f}')

class PolttomoottoriAuto(Auto):
    def __init__(self, rekisteri, huippunopeus,tamanhetkinenNopeus, kuljettuMatka, bensatankinKoko):
        self.bensatankinKoko = bensatankinKoko
        super().__init__(rekisteri, huippunopeus, tamanhetkinenNopeus, kuljettuMatka)
    def tulosta_tiedot(self):
        print(f'Rekisteri: {self.rekisteri} kuljettu matka: {self.kuljettuMatka:.0f}')

autot = []
autoS = SahkoAuto('ABC-15', 180, 0, 0, 52.5)
autoB = PolttomoottoriAuto('ABC-123', 165, 0, 0, 32.3)
autot.append(autoS)
autot.append(autoB)
aika = 0.1
kulunut_aika = 0
while kulunut_aika < 3:
    for i in range(len(autot)):
        muutos = random.randint(-10, 15)
        autot[i].kiihdyta(muutos)
        autot[i].kulje(aika)
    kulunut_aika = kulunut_aika + 0.1
for i in range(len(autot)):
    autot[i].tulosta_tiedot()