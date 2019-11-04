import math
import sys
suma_lini =0
suma_liczb = 0
suma_3 = 0
f = open("dupa.txt", "r")
s= f.readline()
min = float(s)
max = float(s)
min1 = sys.float_info.max
min2 =sys.float_info.max
min3 = sys.float_info.max
while s!= '':
    d = float(s)
    suma_lini+=1
    suma_liczb+=d

    if d<min3:
        if d<min2:
            if d<min3:
                min3=min2
                min2=min1
                min1=d
            else:
                min3 = min2
                min2= d
        else:
            min3 = d
    if d<min:
        min = d
    if d>max:
        max = d


    s =f.readline()

f.seek(0)
s = f.readline()

while s!= "":
    d = float(s)
    a = (d-(suma_liczb/suma_lini))**2
    suma_3+=a
    s = f.readline()

print(suma_liczb)
print(suma_lini)
print(max)
print(min)

f.close()
f = open("statystyki.txt", "w")
f.write(str(suma_liczb))
f.write('\n')
f.write(str(suma_lini))




