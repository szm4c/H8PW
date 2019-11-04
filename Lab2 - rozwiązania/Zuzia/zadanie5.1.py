wejscie = input()
print(wejscie)
liczba1=0
liczba2=0
k=-1
for i in range(len(wejscie)):
    if (wejscie[i]!='1' and wejscie[i]!='0'):
        k=0
    elif (k==-1 and wejscie[i]=='1'):
        liczba1 = liczba1+pow(2,int(i))
    elif (k>=0):
        if (wejscie[i]=='1'):
            liczba2 = liczba2+pow(2,int(k))
        k+=1

print(f"{liczba1}+{liczba2}={liczba1+liczba2}")
if (liczba1>liczba2):
    print('pierwsza')
else: print('druga')