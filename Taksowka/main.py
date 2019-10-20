KWOTA_STARTOWA = 10
CENA_STREFA_I = 2.5
CENA_STREFA_II = 5
PROMIEN_PIERWSZEJ_STREFY = 20

print("Ile masz gotówki przy sobie?")
iloscGotowki = float(input())

if iloscGotowki < 0:
    print("Wprowadzono błędne dane")
    exit()
elif iloscGotowki < 10:
    print("Nie stać cię na taksówkę")

print("Jak daleko jesteś od domu?")
odlegloscOdDomu = float(input())

if odlegloscOdDomu < 0:
    print("Wprowadzono błędne dane")
    exit()
elif odlegloscOdDomu == 0:
    print("Jesteś w domu")
    exit()

print(f"Jesteś oddalony o {odlegloscOdDomu} km od domu i masz przy sobie {iloscGotowki} zł")

iloscGotowki -= KWOTA_STARTOWA      #pobieram opłatę początkową

if iloscGotowki <=50:
    odlJakaMozemyPrzejechac = iloscGotowki // CENA_STREFA_I
else:
    pozostalaGotowka = iloscGotowki - 50
    odlJakaMozemyPrzejechac = 20 + pozostalaGotowka // CENA_STREFA_II

print(f"Możesz przejechać {odlJakaMozemyPrzejechac} km")

if odlJakaMozemyPrzejechac >= odlegloscOdDomu:
    print("Uda ci się dojechać do domu")
else:
    print("Nie uda ci się dojechać do domu")









