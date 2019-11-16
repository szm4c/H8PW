def sqrt1(y,n):
    assert y>0 and y<2
    assert n>0
    a_0 = 1
    suma = 1
    for j in range (1,n-1):
        alfa = (y-1) * ((-2j-1)/2j)
        a_0 *=alfa
        suma = suma + a_0
    return suma

print(sqrt1(1.1,2))