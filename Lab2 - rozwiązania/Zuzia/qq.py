import random
n=10000
random.seed(123)
with  open("dupa.txt", "w") as f:
     for i in range(n) :
       f.write(str(random.uniform(1,100000)))
       f.write('\n')



