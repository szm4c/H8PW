flaga = True         # "stopper" pętli
flagaDwa = True
iloscWartosci = 0
i = 1               # indeks "x"

pierwszaWartosc = int(input("Podaj liczbe: "))
px = pierwszaWartosc         # previous x

if pierwszaWartosc > 1:
    iloscWartosci += 1

    while flaga:
        x = int(input("Podaj liczbe: "))

        if x > px:
            print("Błąd! Podawaj wartości od największej do najmniejszej")
            exit()

        if i >= x and flagaDwa:
            h = x
            flagaDwa = False    # chce żeby to się stało tylko raz

        if x >= 0:
            iloscWartosci += 1
        else:
            flaga = False

        px = x
        i += 1
elif pierwszaWartosc == 1:
    h = 1
elif pierwszaWartosc < 1 and pierwszaWartosc >= 0:
    iloscWartosci += 1
    h = 0
else:
    h = 0


print(f"Podano {iloscWartosci} wartości nieujemnych")
print(f"Indeks h wynosi {h}")

    