Suku = input('Anna sukupuoli: ')
Arvo = float(input('Anna hemoglobiiniarvo (g/l): '))

if Suku == 'Mies' or Suku == 'mies':
    if Arvo < 134:
        print('Hemoglobiini on alhainen.')
    elif 134 <= Arvo <= 195:
        print('Hemoglobiini on normaali.')
    elif Arvo > 195:
        print ('Hemoglobiini on korkea.')
elif Suku == 'Nainen' or Suku == 'nainen':
    if Arvo < 117:
        print('Hemoglobiini on alhainen.')
    elif 117 <= Arvo <= 175:
        print('Hemoglobiini on normaali.')
    elif Arvo > 175:
        print('Hemoglobiini on korkea.')
else:
    print('Tarkista oikeinkirjoitus.')