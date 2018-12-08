import csv

plik = "moneypl.csv"
posiadane_akcje = {"CD Projekt SA": 10,
                   "Santander Bank Polska SA": 5,
                   "Yolo SA": 50}


def akcje(plik, posiadane_akcje):
    wartosc_akcji = 0
    with open(plik, "r", encoding="utf-8-sig") as file:
        kursy = csv.DictReader(file)
        for row in kursy:
            if row["Walor"] in posiadane_akcje:
                wartosc_akcji += (float(row["Kurs (PLN)"]) * float(posiadane_akcje[row["Walor"]]))
        return wartosc_akcji


print(akcje(plik, posiadane_akcje))
