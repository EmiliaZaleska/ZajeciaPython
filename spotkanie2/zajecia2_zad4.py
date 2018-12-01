def pierwsze(n):
    lista_k = []
    for k in range(1, n+1):
        if n % k == 0:
            lista_k.append(k)
    if len(lista_k) == 2:
        print("To jest liczba pierwsza")
    else:
        print("To nie jest liczba pierwsza")


pierwsze(7)

