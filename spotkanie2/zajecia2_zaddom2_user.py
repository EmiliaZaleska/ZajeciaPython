def gra_gracza(liczba_zapalek):
    ruch_gracza = int(input("Podaj swój ruch: "))
    while ruch_gracza > 3:
        print("Nieprawidłowy ruch.")
        ruch_gracza = int(input("Spróbuj ponownie: "))
    liczba_zapalek = liczba_zapalek - ruch_gracza
    print("Pozostalo zapalek: " + str(liczba_zapalek))
    return liczba_zapalek
