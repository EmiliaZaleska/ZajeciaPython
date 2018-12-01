masa = float(input("Podaj masę [kg]: "))
wzrost = float(input("Podaj wzrost [m]: "))


def bmi(masa, wzrost):
    wskaznik_bmi = round((masa / pow(wzrost, 2)), 2)
    if wskaznik_bmi < 18.5:
        print("BMI = " + str(wskaznik_bmi) + " - niedowaga")
    elif 18.5 <= wskaznik_bmi < 24.99:
        print("BMI = " + str(wskaznik_bmi) + " - wartość prawidłowa")
    else:
        print("BMI = " + str(wskaznik_bmi) + " - nadwaga")


print(bmi(masa, wzrost))

# testy
print(bmi(80, 1.80))
print(bmi(120, 1.75))
print(bmi(35, 1.70))
