import random

def stworzLiczby(n = 10):
    liczby = open("liczby.txt", "w")

    for i in range(n):
        a = random.uniform(-1000, 1000)
        liczby.write(f"{a}\n")

    liczby.close()

def stats():
    file = open("liczby.txt", "r")

    dlugoscCiagu = 0
    wartoscMax = -1000
    wartoscMin = 1000
    sumaLiczb = 0
    sumaPotegiRoznicy = 0

    for i in file:
        dlugoscCiagu += 1

        aktualnyFloat = float(i)
        if aktualnyFloat >= wartoscMax:
            wartoscMax = aktualnyFloat

        if aktualnyFloat <= wartoscMin:
            wartoscMin = aktualnyFloat

        sumaLiczb += float(i)

    sredniaArytmetyczna = sumaLiczb / dlugoscCiagu

    for i in file:   #ponownie przelatuje przez plik bo potrzebuje sredniej arytmetycznej liczonej po poprzedniej pętli
        sumaPotegiRoznicy += (float(i) - sredniaArytmetyczna)**2  #wzory wziąłem z neta

    wariancjaProbkowa = (1/(dlugoscCiagu-1))*sumaPotegiRoznicy
    odchylenieStandardowe = (1/dlugoscCiagu)*sumaPotegiRoznicy

    file.close()

    statystyki = open("statystyki.txt", "w")

    statystyki.write(f"1.| Długość ciągu         | {dlugoscCiagu}\n")
    statystyki.write(f"2.| Wartość maksymalna    | {wartoscMax}\n")
    statystyki.write(f"3.| Wartość minimalna     | {wartoscMin}\n")
    statystyki.write(f"4.| Średnia arytmetyczna  | {sredniaArytmetyczna}\n")
    statystyki.write(f"5.| Wariancja próbkowa    | {wariancjaProbkowa}\n")
    statystyki.write(f"6.| Odcylenie standardowe | {odchylenieStandardowe}\n")
    statystyki.write(f"7.| Średnia 1-ucięta      | {wartoscMin}\n")
    statystyki.write(f"8.| Średnia 3-ucięta      | {wartoscMin}\n")

    statystyki.close()

stats()
