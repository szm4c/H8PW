
sumaPierwszej = 0                 #zmienna w ktorej bede liczył sumę pierwszej liczby binarnej
sumaDrugiej = 0                   # to samo tylko ze drugiej

pierwszaNieBinarna = False        # dzieki temu bede wiedzial czy podawane sa cyfry pierwszej czy drugiej liczby,
drugaNieBinarna = False           # innymi słowy bede wiedział czy cyfra nie bedaca 0 i 1 byla wpisana

i = 0
j = 0
while drugaNieBinarna == False:

    cyfra = input(f"Podaj {i+1} cyfrę: ")    # kazda cyfra jest podawana oddzielnie
    cyfraDzies = int(cyfra) * 2**i           # przeliczam pojedyncza cyfre z binarnego na dziesietny
    cyfraDziesBis = int(cyfra) * 2**j        # potem bede decydowal czy uzywam cyfry czy cyfry bis

    if pierwszaNieBinarna:                   # j zwiekszam tylko gdy wpisywana jest juz druga liczba
        j += 1

    if int(cyfra) == 0 or int(cyfra) == 1:   # sprawdzam czy zostaly wpisane 0 lub 1
        if pierwszaNieBinarna == False:
            sumaPierwszej += cyfraDzies      # sumuje pierwsza liczbe
            print(f"suma pierwszej {sumaPierwszej}")     # zbedna linijka, sprawdzalem nia czy wszystko dziala
        else:
            sumaDrugiej += cyfraDziesBis     # sumuje druga, ale tylko wtedy, gdy zostala wpisana cyfra inna niz 0 lub 1
            print(f"suma drugiej {sumaDrugiej}")  # zbedna linijka

    else:        # jezeli nie zostala wpisana ani 1 ani 0, oznacza to dowolna inna liczbe, wiec "koncze" sumowanie
        if pierwszaNieBinarna == True:    # pierwszej i zaczynam drugiej
            drugaNieBinarna = True
        else:                             # jezeli padla juz liczba niebedaca 0 lub 1 to drugaNieBinarna = True, co
            pierwszaNieBinarna = True     # konczy pętle

    i += 1

suma = sumaPierwszej + sumaDrugiej
print(f"Suma tych liczb wynosi {suma}")

if sumaPierwszej > sumaDrugiej:
    print("Pierwsza jest większa")
elif sumaDrugiej > sumaPierwszej:
    print("Druga jest większa")
else:
    print("Liczby są sobie równe")






