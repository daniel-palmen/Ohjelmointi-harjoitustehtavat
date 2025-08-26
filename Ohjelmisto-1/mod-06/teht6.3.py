
def muunnin (gallon):
    litra = gallon * 3.785
    return litra

i = 0
print('Ohjelma muuntaa gallonat litroiksi.')
print('Negatiivinen luku sulkee ohjelman.')
while i == 0:
    gallon = float(input('Anna bensiinin määrä gallonoina: '))
    if gallon <= 0:
        print('Kiitos ohjelman käytöstä.')
        break 
    litra = muunnin(gallon)
    print(f'{gallon} gallonaa on {litra} litraa.')