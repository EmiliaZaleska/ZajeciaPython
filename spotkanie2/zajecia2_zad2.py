def odsetki(oproc, czas, kwota):
    odsetki = kwota * oproc * (czas/12)
    kwota = kwota + odsetki
    return kwota, odsetki


def odsetki2(oproc, czas, kwota):
    i= 0
    suma_odsetek = 0
    while i < 4:
        odsetki2 = kwota * oproc * (czas/12)
        kwota = kwota + odsetki2
        i = i + 1
        suma_odsetek = suma_odsetek + odsetki2
    return kwota, suma_odsetek


print(odsetki(0.03, 12, 1000))
print(odsetki2(0.03, 3, 1000))
