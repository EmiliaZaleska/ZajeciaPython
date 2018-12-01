import random
from spotkanie2.zajecia2_zaddom2_user import gra_gracza


def gra_komputera(liczba_zapalek):
    if liczba_zapalek > 3:
        ruch_komputera = random.randint(1, 3)
        liczba_zapalek = liczba_zapalek - ruch_komputera
        print("Ruch komputera: " + str(ruch_komputera))
        print("Pozostalo zapalek: " + str(liczba_zapalek))
        return liczba_zapalek
    elif liczba_zapalek == 3:
        ruch_komputera = random.randint(1, 2)
        liczba_zapalek = liczba_zapalek - ruch_komputera
        print("Ruch komputera: " + str(ruch_komputera))
        print("Pozostalo zapalek: " + str(liczba_zapalek))
        return liczba_zapalek
    elif liczba_zapalek == 1 or 2:
        ruch_komputera = random.randint(1, 1)
        liczba_zapalek = liczba_zapalek - ruch_komputera
        print("Ruch komputera: " + str(ruch_komputera))
        print("Pozostalo zapalek: " + str(liczba_zapalek))
        return liczba_zapalek


def gra():
    ilosc_zapalek = random.randint(7, 50)
    print("Startowe zapalki: " + str(ilosc_zapalek))
    while ilosc_zapalek > 0:
        ilosc_zapalek = gra_gracza(ilosc_zapalek)
        if ilosc_zapalek == 0:
            return print("Niestety, przegrałeś! :(")
        ilosc_zapalek = gra_komputera(ilosc_zapalek)
        if ilosc_zapalek == 0:
            return print("Brawo, wygrałes! :)")


gra()

