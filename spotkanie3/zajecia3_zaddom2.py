plik = "krol-lear.txt"
plik_porownawczy = "sen-nocy-letniej.txt"

# plik = "testtest.txt"
# plik_porownawczy = "testtest2.txt"


def statystyka(plik):
    with open(plik, 'r', encoding='utf-8-sig') as file:
        tekst = file.read().lower()

    znaki = "()*?.!/0123456789,:;--"
    for znak in znaki:
        tekst = tekst.replace(znak, "")
    tekst = tekst.split()
    slownik_wystapienia = {}
    for slowo in sorted(tekst):
        slownik_wystapienia[slowo] = tekst.count(slowo)
    return slownik_wystapienia


print(statystyka(plik))
print(statystyka(plik_porownawczy))


def porownanie(plik, plik_porownawczy, wartosc):
    slownik1 = statystyka(plik)
    slownik2 = statystyka(plik_porownawczy)
    lista_unikatow_slownik1 = []
    lista_unikatow_slownik2 = []
    lista_czestotliwosci = []
    for klucz in slownik1:
        if klucz not in slownik2:
            lista_unikatow_slownik1.append(klucz)
    for klucz in slownik2:
        if klucz not in slownik1:
            lista_unikatow_slownik2.append(klucz)
    for klucz in slownik1:
        if klucz in slownik2:
            if abs((slownik2[klucz]) - (slownik1[klucz]) == wartosc):
                lista_czestotliwosci.append(klucz)
    print("Lista słów unikatowych w pliku " + plik + ": " + str(lista_unikatow_slownik1))
    print("Lista słów unikatowych w pliku porownawczym " + plik_porownawczy + ": " + str(lista_unikatow_slownik2))
    print("Lista słów o częstotliwości różniącej się o zadaną wartość = " + str(wartosc) + ": "
          + str(lista_czestotliwosci))


porownanie(plik, plik_porownawczy, 2)
