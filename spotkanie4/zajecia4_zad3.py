class Wyrazenie:
    pass


class Zmienna(Wyrazenie):
    def __init__(self, zmienna):
        self.zmienna = zmienna

    def __str__(self):
        return self.zmienna

    def oblicz(self, stan):
        return stan[self.zmienna]

class Stala(Wyrazenie):
    def __init__(self, stala):
        self.stala = stala

    def __str__(self):
        return str(self.stala)

    def oblicz(self, stala):
        return self.stala

class Dodawanie(Wyrazenie):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return "(" + str(self.left) + "+" + str(self.right) + ")"

    def oblicz(self, stan):
        return self.left.oblicz(stan) + self.right.oblicz(stan)

    def uprosc(self):
        #return "Stala(" + str(self.left.oblicz(Stala) + self.right.oblicz(Stala))+ ")"

        return Stala((self.left.oblicz(Stala) + self.right.oblicz(Stala)))


class Mnozenie(Wyrazenie):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return "(" + str(self.left) + "*" + str(self.right) + ")"

    def oblicz(self, stan):
        return self.left.oblicz(stan) * self.right.oblicz(stan)



wyrazenie1 = Dodawanie(Zmienna("x"), Zmienna("y"))
stan = {"x": 2, "y": 3}
print("{0} = {1}".format(wyrazenie1, wyrazenie1.oblicz(stan)))
wyrazenie2 = Mnozenie(Zmienna("x"), Zmienna("y"))
stan = {"x": 2, "y": 3}
print("{0} = {1}".format(wyrazenie2, wyrazenie2.oblicz(stan)))
wyrazenie3 = Dodawanie(Stala(4), Stala(6))
print("{0} = {1}".format(wyrazenie3, wyrazenie3.oblicz(0)))
wyrazenie4 = Mnozenie(Stala(4), Stala(6))
print("{0} = {1}".format(wyrazenie4, wyrazenie4.oblicz(0)))
wyrazenie5 = Dodawanie(Stala(4), Stala(6))
nowe = wyrazenie5.uprosc()
print(nowe)
wyrazenie6 = Dodawanie(nowe, Stala(5))
print("{0} = {1}".format(wyrazenie6, wyrazenie6.oblicz(0)))