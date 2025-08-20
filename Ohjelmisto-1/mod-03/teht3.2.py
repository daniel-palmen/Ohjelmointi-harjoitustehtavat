Luokka = input('Anna hyttiluokka: ')

if Luokka == 'LUX' or Luokka == 'lux':
    print(f'{Luokka} on parvekkeellinen hytti yläkannella.')
elif Luokka == 'A' or Luokka == 'a':
    print(f'{Luokka} on ikkunallinen hytti autokannen yläpuolella.')
elif Luokka == 'B' or Luokka == 'b':
    print(f'{Luokka} on ikkunaton hytti autokannen yläpuolella.')
elif Luokka == 'C' or Luokka == 'c':
    print(f'{Luokka} on ikkunaton hytti autokannen alapuolella')
else:
    print('virheellinen hyttiluokka')