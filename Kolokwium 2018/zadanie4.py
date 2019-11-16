def repeat(x, t):
    '''
    n = len(x)
    m = len(t)
    assert n == m and n != 0 #and m!=0
    sum=0
    for k in range(m):
        sum += t[k]
    z = [None] * sum






    return z
    '''

    n = len(x)
    m = len(t)
    suma = 0

    for i in range(m):
        suma += t[i]

    print(f"suma: {suma}")

    w = [None] * suma
    print(f"dlugosc w = {suma}\n")
    k = 0

    for i in range(n):
        print(f"    i = {i}")

        for j in range(t[i]):
            print(f"        j = {j}")

            w[k] = x[i]

            print(f"        k = {k}")
            print(f"        w[{k}] = {w[k]}")
            print("        koniec iteracji j\n")
            k += 1

        print("    koniec iteracji i\n")

    return w

print(repeat([1, 2, 3, 4], [1, 2, 3, 4]))
print(repeat([1,2,3,4,5],[5,0,0,3,0]))