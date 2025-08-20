Tuuma = 0
while Tuuma >= 0:
    Tuuma = float(input('Anna mitta tuumina: '))
    if Tuuma < 0:
        break
    Sentti = 2.54 * Tuuma
    print(f'{Tuuma} tuumaa on {Sentti} senttiä.')