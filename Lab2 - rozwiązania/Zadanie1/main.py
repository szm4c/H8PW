m = 2**31 - 1
a = 1103515245
c = 12345

s = int(input("Podaj ziarno generatora: "))
n = int(input("Podaj liczbe wartości do wygenerowania: "))

print(f"Ziarno generatora wynosi: {s} \nLiczba wartości do wygenerowania: {n}")

file = open("liczby.txt", "w")

ps = s
i = 0
while i < n:
    s = (a*ps + c) % m
    ps = s
    file.write(f"{i+1}. Liczba losowa - {s}\n")
    i += 1



