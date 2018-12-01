def liczenie_podatku(kwota):
    if kwota <= 44490:
        return 0.19 * kwota
    elif 44490 < kwota <= 85528:
        return 0.30 * (kwota-44490) + 0.19 * 44490
    elif kwota > 85528:
        return 0.40 * (kwota-85528) + 0.30 * 41038 + 0.19 * 44490


print(round(liczenie_podatku(100000)))

