def suma_dzielnikow(n):
    suma = 0
    lista = []
    for k in range(1, n):
        if n % k == 0:
            suma = k + suma
            lista.append(k)
    return suma


def pierwsze(n):
    lista_k = []
    for k in range(1, n+1):
        if n % k == 0:
            lista_k.append(k)
    if len(lista_k) == 2:
        return True
    else:
        return False


def dzielniki_pierwsze(n):
    lista_pierwsze_dzielniki = []
    for k in range(1, n):
        if n % k == 0:
            if pierwsze(k):
                lista_pierwsze_dzielniki.append(k)
    return lista_pierwsze_dzielniki


#print(dzielniki_pierwsze(34))

def doskonala(n):
    return suma_dzielnikow(n) == n


print(doskonala(27))
