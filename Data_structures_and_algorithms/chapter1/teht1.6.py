sum = 0
while 1==1:
    luku = input()
    if luku.isdigit():
        luku = float(luku)
        if luku == 0:
            print(f'The grand total is {sum:.1f}')
            break
        sum = sum + luku
        print(f'The total is now {sum:.1f}')
    else:
        print("That wasn't a number.")