import re
nazwa_pliku = "test.txt"


def statystyka(nazwa_pliku):
    with open(nazwa_pliku, 'r') as file:
        tekst = file.read()

    liczba_znakow = "Liczba znaków: " + str(len(tekst))
    liczba_slow = "Liczba słów: " + str(len(tekst.split()))
    if str(re.split(r"[.!?]", tekst)[-1]) == "":
        liczba_zdan = "Liczba zdań: " + str(int(len(re.split(r"[.!?]", tekst))) - 1)
    else:
        liczba_zdan = "Liczba zdań: " + str(len(re.split(r"[.!?]", tekst)))
    return liczba_znakow, liczba_slow, liczba_zdan


print(statystyka(nazwa_pliku))
