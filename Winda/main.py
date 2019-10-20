
def winda(n, m):
    #print("Podaj liczbę osób na dole:")
    #n = int(input())
    if n < 0:
        print("Błędne dane")
        exit()
    #print("Podaj liczbę osób na górze:")
    #m = int(input())
    if m < 0:
        print("Błędne dane")
        exit()

    if n > m:
        iloscKursow = 2 * (n // 8) - 1
    elif n == m:
        if n % 8 != 0:
            iloscKursow = 2 * (m // 8 + 1)
        else:
            iloscKursow = 2 * (m // 8)
    else:
        if m % 8 == 0:
            iloscKursow = 2 * (m // 8)
        else:
            iloscKursow = 2 * (m // 8 + 1)

    print(iloscKursow)
    return iloscKursow

print("Podaj liczbę osób na dole:")
n = int(input())

print("Podaj liczbę osób na górze:")
m = int(input())

winda(n, m)
winda(0, 0)
winda(20, 0)
winda(0, 10)
winda(30, 72)
winda(54, 8)
winda(8, 8)