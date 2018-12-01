lista = ([["to", "bedzie", "pierwsze", "zdanie"], ["a", "teraz", "zdanie", "drugie"]])


def zbuduj_zdania(lista):
    zdanie = ""
    for element in lista:
        dlugosc_zdania = int(len(element))
        for i in range(0, (len(element)-1)):
            element[i] = element[i]+" "
        element.append(". ")
        zdanie = zdanie + ("".join(element)).capitalize()
    return zdanie



print(zbuduj_zdania(lista))