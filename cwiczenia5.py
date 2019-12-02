def wypisz(macierz): #zeby widziec wiecej
    for i in range(len(macierz)):
        print(f"{macierz[i]}")

def hilbert(n):   #cwiczenie1
    h = [[0 for i in range(n)] for j in range(n)]  #kolumny * wiersze

    for a in range(1, n+1):
        for b in range(1, n+1):
            h[a-1][b-1] = 1 / (a + b - 1)

    return h

#wypisz(hilbert(4))

def tr(A):  #cwiczenie2
    n = len(A)
    assert len(A) == len(A[0]), "macierz nie jest kwadratowa"
    suma = 0

    for i in range(n):
        suma += A[i][i]

    return suma

#print(tr(hilbert(4)))

def czy_symetryczna(macierz):  #cwiczenie 3
    n = len(macierz)  #pobralismy ilosc wierszy
    assert n == len(macierz[0]), "macierz musi być kwadratowa"

    for i in range(n):
        for j in range(n):
            if macierz[i][j] != macierz[j][i]:
                return False
    return True

#print(czy_symetryczna((hilbert(4))))

#cw 4 czym jest diagonala???

def mnozenie(A, k):  #cwiczenie 5
    w = len(A)
    kol = len(A[0])

    for i in range(kol):
        for j in range(w):
            A[i][j] *= k

    return A

#print(mnozenie(hilbert(4), 10))

#cw 6 mnozenie macierzy???? kazdy el przez siebie? jak?
#cw 7 o co chodzi masakra

def transpoze(A):  #cwiczenie 8 robione na labach w sumie
    n = len(A)  #wiersze
    m = len(A[0])  #kolumny

    B = [[0 for i in range(n)] for j in range(m)] #nowa macierz, zamieniamy dl kolumn i wierszy

    for i in range(n):
        for j in range(m):
            B[j][i] = A[i][j]

    return B

macierz = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]]
#wypisz(macierz)
#wypisz(transpoze(macierz))

def wstaw_wiersz(A, b, i):  #cwiczenie 9
    assert len(A[0]) == len(b), "wiersz musi byc tej samej dlugosci co inne wiersze w liscie"
    assert i >= 0 and i < len(A) + 1, "wiersz trzeba wstawic na 0-n pozycji"  #len(A) +1 żebyśmy mogli wstawić na ostatnie miejsce

    B = [[0 for a in range(len(A[0]))] for b in range(len(A) + 1)] #tworzymy macierz, ktora ma jeden wiersz wiecej

    for n in range(i):
            B[n] = A[n]

    B[i] = b #wstawiamy wiersz

    m = len(B) - 1 #od ostatniego indeksu

    while m != i:  #uzupelniamy wierszami z A
        B[m] = A[m - 1]
        m -= 1

    return B

#wypisz(wstaw_wiersz(macierz, [0, 0, 0], 4))

def wstaw_kolumne(A, b, i):  #cwiczenie 10
    n = len(A)  #ilosc wierszy
    m = len(A[0]) #ilosc kolumn

    assert len(b) == n, "kolumna musi byc tak samo dluga jak kolumny w macierzy"
    assert i >= 0 and i <= m, "wstawiamy na istniejące miejsce"

    B = [[0 for a in range(m+1)] for c in range(n)]  #nowa macierz, ktora ma o kolumne wiecej

    for c in range(n):  #zapelniamy lewa strone takimi kolumnami jakie byly
        for a in range(i):
            B[c][a] = A[c][a]

    for j in range(n):
            B[j][i] = b[j]
    #uzupelniamy
    for c in range(i+1, m+1):  #kolumna od i+1
        for a in range(n):  #wiersz od poczatku
            B[a][c] = A[a][c-1]

    return B

#wypisz(wstaw_kolumne(macierz, [0, 0, 0, 0, 0], 1))

#naprawic cwiczenie 11
'''
def usun(A, i, j):
    n = len(A)
    m = len(A[0])

    assert 0 <= i-1 < n and 0 <= j-1 < m, "zle numery kolumn/wierszy"  #mniejsze o 1 bo wywala blad inaczej - komputer indeksuje inaczej

    B = [[0 for k in range(m-1)] for w in range(n-1)]  #tworzymy mniejsza macierz

    for k in range(j):  #wypelnienie do pewnego momentu tym czego nie usuwamy
        for w in range(i):
            B[w][k] = A[w][k]


    for k in range(j+1, len(B[0])):   #pomijamy jeden wiersz i jedna kolumne
        for w in range(i+1, len(B)):
            B[w][k] = A[w][k]

    return B

usun([macierz], 1, 1)
'''