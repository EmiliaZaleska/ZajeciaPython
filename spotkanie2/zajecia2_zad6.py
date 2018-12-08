lista_imion = ["Piotr", "Maria", "Jan", "Kamil", "Kamila", "Magda", "Anna", "Stefan", "Halina"]


def porzadek(lista_imion):
    lista_imion.sort()
    print(lista_imion)


def imiona_zenskie(lista_imion):
    liczba_zenskie = 0
    for element in lista_imion:
        if element[-1] == "a":
            liczba_zenskie += 1
    return liczba_zenskie


porzadek(lista_imion)
print(imiona_zenskie(lista_imion))
