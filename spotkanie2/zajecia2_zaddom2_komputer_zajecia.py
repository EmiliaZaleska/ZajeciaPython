import random


def strategia(stan_gry):
    ruch = min(stan_gry, random.randint((1, 3)))
    return ruch