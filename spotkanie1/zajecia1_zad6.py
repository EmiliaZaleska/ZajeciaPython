#def suma_dzielnikow(n):
#   suma = 0
#    for k in range(1, n):
#        if n % k == 0:
#            suma = k + suma
#    return suma

def suma_dzielnikow(n):
    suma = 0
    lista = []
    for k in range(1, n):
        if n % k == 0:
            suma = k + suma
            lista.append(k)
    return lista

print(suma_dzielnikow(6))

