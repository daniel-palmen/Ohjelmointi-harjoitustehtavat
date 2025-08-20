pituus = float(input('Syötä kuhan pituus sentteinä: '))
laillinen = 37
if pituus < laillinen:
    puutos = laillinen - pituus
    print(f'Laske kuha veteen, se on {puutos:.2f} senttiä liian lyhyt.')
else:
    print('Kuha on sallitun mittainen.')