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
Auto = auto('ABC-123', 142, 0, 0)
print(Auto)
Auto.kiihdyta(30)
Auto.kiihdyta(70)
Auto.kiihdyta(50)
print(Auto.tamanhetkinenNopeus)
Auto.kulje(1)
Auto.kiihdyta(-200)
print(Auto.tamanhetkinenNopeus)
print(Auto)
