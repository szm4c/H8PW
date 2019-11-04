import random
import math
def przyblizPi(n):
    suma = 0
    n=100000
    for i in range(n):
        x = random.uniform(-1,1)
        y = random.uniform(-1,1)
        if math.sqrt(x**2 + y**2)<= 1:
            suma+=1
            a= suma*4
            b=a/n
    return (b)
