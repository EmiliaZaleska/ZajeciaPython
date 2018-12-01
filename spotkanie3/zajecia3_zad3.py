nazwa_pliku = "test.txt"


def statystyka(nazwa_pliku):
    with open(nazwa_pliku,'r') as fh:
        tekst = fh.read()
        liczba_znakow = "Liczba znaków: " + str(len(tekst))
        liczba_slow = "Liczba słów: " + str(len(tekst.split()))
        if str(tekst.split(".")[-1]) == "":
            liczba_zdan = "Liczba zdań: " + str(int(len(tekst.split("."))) - 1)
        else:
            liczba_zdan = "Liczba zdań: " + str(len(tekst.split(".")))
        return liczba_znakow, liczba_slow, liczba_zdan

print(statystyka(nazwa_pliku))