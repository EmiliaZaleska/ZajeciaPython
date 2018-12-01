import random

tekst = "Podział peryklinalny inicjalów wrzecionowatych kambium charakteryzuje się ścianą podziałową inicjowaną w płaszczyznie maksymalnej"


def uprosc_zdanie(tekst, dl_slowa, liczba_slow):
    tekst = tekst.split()
    result = []
    for slowo in tekst:
        if len(slowo) <= dl_slowa:
            result.append(slowo)
    tekst = result
    while len(tekst) > liczba_slow:
        losowe_slowo = (tekst[random.randint(0, (len(tekst)-1))])
        tekst.remove(losowe_slowo)
    return " ".join(tekst)


print(uprosc_zdanie(tekst, 10, 4))
print(uprosc_zdanie(tekst, 4, 3))
print(uprosc_zdanie(tekst, 8, 2))