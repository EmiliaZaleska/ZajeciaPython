cennik = {
    'kawa': 14.99,
    'pomarancze': 3.49,
    'olej': 4.99
}

lista = {'olej': 2, 'kawa': 1}


def zakupy(cennik, lista):
    suma = 0
    kwota = 0
    podatek = 0
    for artykul in lista:
        if artykul in cennik:
            kwota = (float(cennik[artykul]) * float(lista[artykul])) + (round(0.23 * float(cennik[artykul]), 2) * float(lista[artykul]))
            suma = suma + kwota
    return round(suma, 2)


print(zakupy(cennik, lista))

