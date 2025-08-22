import random
Maara = int(input('Anna heitettävien arpakuutioiden määrä: '))
i = 0
Lista = []
while Maara != i:
    i = i + 1
    Noppa = random.randint(1,6)
    Lista.append(Noppa)
    
print(Lista)