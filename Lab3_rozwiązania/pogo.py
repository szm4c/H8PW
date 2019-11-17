
def czy_sie_przewroci(wysokosci_schodkow, wys_pierw):
    ilosc_schodkow = len(wysokosci_schodkow)
    spadek = wys_pierw

    for i in range(1, ilosc_schodkow):
        if spadek > 100:
            return True
        else:
            spadek = wysokosci_schodkow[i] + (spadek / 2)

    return False

def ile_skokow(wysokosci_schodkow):
    ilosc_schodkow = len(wysokosci_schodkow)
    spadek = wysokosci_schodkow[0]
    numer_skoku = 1

    for i in range(1, ilosc_schodkow):
        if spadek > 100:
            return numer_skoku
        else:
            spadek = wysokosci_schodkow[i] + (spadek / 2)
            numer_skoku += 1

    return ilosc_schodkow

def podaj_wys_pierw(wysokosci_schodkow):
    wys_pierw = 1
    while wys_pierw <= 100:

        if czy_sie_przewroci(wysokosci_schodkow, wys_pierw):
            return wys_pierw

        wys_pierw += 1

    return 101

def main():
    x_string = input("Podaj wysokości schodków: ")

    x = x_string.split()
    wysokosci_schodkow = [None] * len(x)

    for i in range(len(x)):
        wysokosci_schodkow[i] = int(x[i])

    assert len(wysokosci_schodkow) != 0, "Nie podałeś żadnej wysokości!"

    print(f"Skoczek wykona {ile_skokow(wysokosci_schodkow)} skoków")
    print(f"Najmniejsza wysokość pierwszego schodka gwarantująca sukces: {podaj_wys_pierw(wysokosci_schodkow)}")

main()