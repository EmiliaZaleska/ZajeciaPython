from math import *


def funkcja_ackermanna(m,n):
    if m == 0:
        wynik = n + 1
        return wynik
    if m > 0 and n == 0:
        wynik = funkcja_ackermanna(m-1,1)
        return wynik
    if m > 0 and n > 0:
        wynik = funkcja_ackermanna(m-1,funkcja_ackermanna(m, n-1))
    return wynik

print(funkcja_ackermanna(3,3))