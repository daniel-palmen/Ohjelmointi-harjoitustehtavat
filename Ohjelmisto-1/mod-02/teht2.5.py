Leiviskat_inp = float(input('Anna leiviskät: '))
Naulat_inp = float(input('Anna naulat: '))
Luodit_inp = float(input('Anna luodit: '))

Kluoti = 13.3
Knaula = 13.3 * 32
Kleiviska = Knaula * 20

Summa = Leiviskat_inp * Kleiviska + Naulat_inp * Knaula + Luodit_inp * Kluoti
Kilot = Summa//1000
Grammat = Summa%1000

print('Massa nykymittojen mukaan:')
print(f'{Kilot:.0f} kilogrammaa ja {Grammat:.2f} grammaa.')