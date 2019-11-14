

def odchylenieSd(x):
    import math

    sr_x = sum(x) / len(x)
    licznik = 0

    for i in range(len(x)):
        licznik += (x[i] - sr_x) ** 2

    wynik = math.sqrt(licznik / (len(x)  - 1))

    return wynik

def regresja(x, y):
    if len(x) != len(y):
        print("Podane listy nie są równej długości")
        exit()

    sr_x = sum(x) / len(x)
    sr_y = sum(y) / len(y)
    licznik = 0
    mianownik = 0

    for i in range(len(x)):
        licznik += (x[i] - sr_x) * (y[i] - sr_y)
        mianownik += (x[i] - sr_x) ** 2

    beta = licznik / mianownik
    alpha = sr_y - beta * sr_x

    return [alpha, beta]

def E(alpha, beta, x, y):
    if len(x) != len(y):
        print("Podane listy nie są równej długości")
        exit()

    wynik = 0

    for i in range(len(x)):
        wynik += (alpha + beta * x[i] - y[i]) ** 2

    return wynik

def r(x, y):
    if len(x) != len(y):
        print("Podane listy nie są równej długości")
        exit()

    sr_x = sum(x) / len(x)
    sr_y = sum(y) / len(y)
    suma = 0

    for i in range(len(x)):
        suma += ((x[i] - sr_x) / odchylenieSd(x)) * ((y[i] - sr_y) / odchylenieSd(y))

    wynik = (1 / (len(x) - 1)) * suma

    return wynik

def main():
    import random
    random.seed(123)    #sprawia ze rysunek bedzie zawsze taki sam
    alpha0 = -3
    beta0 = 1.5
    n = 100

    x = [random.uniform(-10, 10) for i in range(n)]
    y = [alpha0 + beta0 * x[i] + random.normalvariate(0, 1) for i in range(n)]
    # czyli y=alpha0+beta0*x+szum z rozkładu normalnego N(0,1)
    import matplotlib.pyplot as plt
    # wykres rozproszenia:
    plt.scatter(x, y)
    # rysowanie odcinka [xmin, xmax], [ymin, ymax]:
    plt.plot([-10, 10], [alpha0 + beta0 * (-10), alpha0 + beta0 * 10], color="red")
    # zapis do pliku PNG:
    plt.savefig("obrazek.png")

main()