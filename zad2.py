import math
def find_interval(t,v):
    n = len(t)
    assert len(t)>0
    for i in range(n-1):
        assert t[i] <= t[i+1]
    lista = [-math.inf,*t, math.inf]
    for i in range (1,n+2):
        if lista[i-1] < v <= lista[i]:
            return i-1



print(find_interval([0],-1))
