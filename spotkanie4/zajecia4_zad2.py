class Osoba:

    def __init__(self, imie, nazwisko, masa, wzrost):
        self.imie = imie
        self.nazwisko = nazwisko
        self.masa = masa
        self.wzrost = wzrost

    def __str__(self):
        return self.__class__.__name__ + self.imie + " " + self.nazwisko

    def bmi(self):
        wskaznik_bmi = round((self.masa / pow(self.wzrost, 2)), 2)
        if wskaznik_bmi < 18.5:
            print("BMI = " + str(wskaznik_bmi) + " - niedowaga")
        elif 18.5 <= wskaznik_bmi < 24.99:
            print("BMI = " + str(wskaznik_bmi) + " - wartość prawidłowa")
        else:
            print("BMI = " + str(wskaznik_bmi) + " - nadwaga")


class Pracownik(Osoba):

    def __init__(self, imie, nazwisko, pensja, masa, wzrost):
        Osoba.__init__(self, imie, nazwisko, masa, wzrost)
        self.pensja = pensja

    def wyplata(self):
        return self.pensja * 1.2

    def __str__(self):
        return "Pracownik: " + self.imie + " " + self.nazwisko


class Kierownik(Pracownik):

    def wyplata(self):
        return super().wyplata() + 1200.0

    def __str__(self):
        return "Kierownik: " + self.imie + " " + self.nazwisko


o = Osoba("Jan",  "Kowalski", 40, 1.60)
print(o)
print(Osoba.bmi(o))

p = Pracownik("Jan", "Nowak", 2250, 80, 1.80)
print(Pracownik.bmi(p))
print("{0} wypłata {1}".format(p, p.wyplata()))
k = Kierownik("Anna", "Testowa", 5000, 100, 1.25)
print(k)
print(Kierownik.bmi(k))
print(k.wyplata())
