class Julkaisu:
    def __init__(self, julkaisu_nimi):
        self.julkaisu_nimi = julkaisu_nimi

class Kirja(Julkaisu):
    def __init__(self, julkaisu_nimi, kirjailija, sivumaara):
        self.kirjailija = kirjailija
        self.sivumaara = sivumaara
        super().__init__(julkaisu_nimi)

    def tulosta_tiedot(self):
        print(f'Julkaisu: {self.julkaisu_nimi} Kirjailija: {self.kirjailija} Sivumäärä: {self.sivumaara}')

class Lehti(Julkaisu):
    def __init__(self, julkaisu_nimi, paatoimittaja):
        self.paatoimittaja = paatoimittaja
        super().__init__(julkaisu_nimi)
    
    def tulosta_tiedot(self):
        print(f'Julkaisu: {self.julkaisu_nimi} Päätoimittaja: {self.paatoimittaja}')

aku = Lehti('Aku Ankka', 'Aki Hyypiä')
hytti = Kirja('Hytti n:o 6', 'Rosa Liksom', 200)
aku.tulosta_tiedot()
hytti.tulosta_tiedot()