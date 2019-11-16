def repeat(x,t):
    assert len(x) >0
    assert len(t)>0
    assert len(x) == len(t)
    n = len(x)
    lista=[]
    for i in range(n):
        for j in range(t[i]):
            lista=[*lista, x[i]]
    return lista

print(repeat([1,2],[1,3]))