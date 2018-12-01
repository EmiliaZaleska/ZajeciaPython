from math import floor

pieniadze = [1, 2, 5, 10, 20]


def liczenie_monet_i_banknotow(kwota_zakupow):
    pozycja_na_liscie = -1
    reszta = kwota_zakupow
    while reszta > 0 and kwota_zakupow > 0:
        nominal = pieniadze[pozycja_na_liscie]
        reszta = kwota_zakupow % nominal
        liczba_sztuk = floor(kwota_zakupow / nominal)
        kwota_zakupow = kwota_zakupow - (liczba_sztuk * nominal)
        print("Nominal: " + str(nominal) + ", sztuk: " + str(liczba_sztuk))
        pozycja_na_liscie = pozycja_na_liscie-1


print(liczenie_monet_i_banknotow(123))

# testy
print(liczenie_monet_i_banknotow(145))
print(liczenie_monet_i_banknotow(19))
print(liczenie_monet_i_banknotow(217))
print(liczenie_monet_i_banknotow(315))
