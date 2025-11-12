
def custom_encoder(str):
    str = str.lower()
    lista = []
    reference_string = 'abcdefghijklmnopqrstuvwxyz'
    for char in str:
        i = 0
        testi = 0
        for r_char in reference_string:
            if char == r_char:
                lista.append(i)
                testi = 1
            else:
                i = i + 1
        if testi == 0:
            lista.append(-1)

    return lista
testi = "gaarmamimaiA"
vastaus = custom_encoder(testi)
print(vastaus)