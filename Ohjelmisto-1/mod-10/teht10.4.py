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

class kilpailu:
    def __init__(self, nimi, pituus, autoLista):
        self.kilpailunNimi = nimi
        self.kilpailunPituus = pituus
        self.kilpailunAutot = autoLista
    def tunti_kuluu(self):
        aika = 1
        for i in range(len(self.kilpailunAutot)):
            muutos = random.randint(-10, 15)
            self.kilpailunAutot[i].kiihdyta(muutos)
            self.kilpailunAutot[i].kulje(aika)
    def tulosta_tilanne(self):
        print('\nKilpailun tämänhetkinen tilanne:')
        for i in range(len(self.kilpailunAutot)):
            print(self.kilpailunAutot[i])
    def kilpailu_ohi(self):
        for i in range(len(self.kilpailunAutot)):
            if self.kilpailunAutot[i].kuljettuMatka >= self.kilpailunPituus:
                print(f'\n~~~Auto {self.kilpailunAutot[i].rekisteri} voitti kisan~~~')
                return True
        return False

autojenMaara = 10
maali = 8000
autoLista = []
kilpailunNimi = 'Suuri Romuralli'
boolean = False
tunnit = 0

for i in range(0, autojenMaara):
    huippu = random.randint(100,200)
    rekisteri = 'ABC-{0}'.format(i + 1)
    autoLista.append(auto(rekisteri, huippu, 0, 0))

kilpailu1 = kilpailu(kilpailunNimi, maali, autoLista)

while boolean == False:
    kilpailu1.tunti_kuluu()
    tunnit = tunnit + 1
    if tunnit % 10 == 0:
        kilpailu1.tulosta_tilanne()
    boolean = kilpailu1.kilpailu_ohi()

kilpailu1.tulosta_tilanne()