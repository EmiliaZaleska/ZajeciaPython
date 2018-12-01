from spotkanie2 import zajecia2_zaddom2_komputer_zajecia

stan_gry = 10
gracz = 0

def ruch_gracza(stan_gry):
    print("Na stole jest {0} zapałek".format(stan_gry))
    ruch = int(input("Podaj liczbe zapalek"))
    return ruch
print("Zaczynamy. Jest {0} zapalek".format(stan_gry))
while stan_gry > 0:
    if gracz == 0:
        ruch = zajecia2_zaddom2_komputer_zajecia.strategia(stan_gry)
    else:
        ruch = ruch_gracza(stan_gry)
    stan_gry = stan_gry - ruch
    print("Wzieto {0} zapale. Zostalo {1}".format(ruch, stan_gry))
    gracz = 1 - gracz