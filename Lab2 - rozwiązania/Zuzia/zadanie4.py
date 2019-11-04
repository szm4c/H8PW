ilość_cukierków = 100

while ilość_cukierków > 0:
    print(ilość_cukierków)
    gracz_1 = int(input("Ile cukierków bierze 1 gracz ?"))
    if ilość_cukierków>gracz_1:
       ilość_cukierków = ilość_cukierków - gracz_1
       print(ilość_cukierków)
       gracz_2 = int(input("ile cukierków bierze 2 gracz? "))
       if gracz_2>= gracz_1:
           print("bląd")
           break
       elif ilość_cukierków>gracz_2:
           ilość_cukierków= ilość_cukierków - gracz_2
       else:
           print("bład")
           break
    else:
        print("bład")
        break



