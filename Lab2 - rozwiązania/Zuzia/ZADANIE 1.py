s = int(input("podaj ziarno:"))
l = int(input("podaj liczbe:"))
plik = open ("aa.txt" ,"w")
for i in range (l):
    m = 2 ** 31 - 1
    a = 1103515245
    c = 12345
    s = (a*s+c) % m
    x = s/m
    plik.write(str(x))
    plik.write("\n")
plik.close()

