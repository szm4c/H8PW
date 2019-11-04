PULA_CUKIERKOW = 100

a = int(input("Ile cukierkow bierze pierwszy gracz: "))
if a >= 100 or a < 1:
    print("Błąd! [KONIEC]")
    exit()
PULA_CUKIERKOW -= a
prvZabrane = a
i = 0

while PULA_CUKIERKOW > 0:
    if i % 2 == 0:
        zabrane = int(input("Ile cukierkow bierze drugi gracz: "))
    else:
        zabrane = int(input("Ile cukierkow bierze pierwszy gracz: "))


    if zabrane > PULA_CUKIERKOW or zabrane > prvZabrane or zabrane <= 0:
        print("Błąd! [KONIEC]")
        exit()
    else:
        PULA_CUKIERKOW -= zabrane

    if PULA_CUKIERKOW == 0:
        if i % 2 == 1:
            print("Wygrał pierwszy gracz!")
            exit()
        else:
            print("Wygrał drugi gracz!")
            exit()
    prvZabrane = zabrane

    i += 1
