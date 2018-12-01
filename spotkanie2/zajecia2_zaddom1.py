portfel = [0, 2, 0, 0, 0, 5, 0, 0, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10]
kwota = 123

def rozmien (portfel, kwota):
    nominaly = []
    sztuki = []
    for nom, lp in enumerate(portfel):
        if lp != 0:
            nominaly.append(nom)
            sztuki.append(lp)
    indeks = -1
    ilosc_nominalow = int(len(nominaly)*-1)
    reszta = kwota
    suma = 0
    while kwota > 0 and reszta > 0 and indeks in range(ilosc_nominalow, 0):
        nominal = nominaly[indeks]
        liczba_sztuk = sztuki[indeks]
        if (nominal * liczba_sztuk) <= reszta:
            reszta = reszta - (nominal * liczba_sztuk)
            print("Nominal: " + str(nominal) + ", sztuk: " + str(liczba_sztuk))
            indeks -= 1
            suma = suma + (nominal * liczba_sztuk)
        elif nominal <= reszta < (nominal * liczba_sztuk):
            liczba_sztuk = reszta // nominal
            reszta = reszta - nominal * liczba_sztuk
            print("Nominal: " + str(nominal) + ", sztuk: " + str(liczba_sztuk))
            indeks -= 1
            suma = suma + nominal * liczba_sztuk
        elif nominal > reszta:
            indeks -= 1
    print("Zrealizowana kwota = " + str(suma))


rozmien(portfel, kwota)
