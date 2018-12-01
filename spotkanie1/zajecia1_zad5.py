def vat_faktura(lista):
    suma = 0
    for element in lista:
        suma = suma + element
    vat = round(0.23 * suma, 2)
    return vat

zakupy = [0.2, 0.5, 4.59, 6]
print("Vat Faktura: ")
print(vat_faktura(zakupy))

def vat_paragon(lista):
    suma_paragon = 0
    for element in lista:
        vat_paragon = round(0.23 * element, 2)
        suma_paragon = suma_paragon + vat_paragon
    return suma_paragon

zakupy = [0.2, 0.5, 4.59, 6]
print("Vat Paragon: ")
print(vat_paragon(zakupy))
