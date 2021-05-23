from random import randrange
import datetime

def losowa(a,b,n):
    matrix=[[randrange(1,n) for i in range(b)] for j in range(a)]
    print('macierz o rozmiarze : '+ str(a)+'x'+str(b))
    return matrix


def detfast(A):
    start = datetime.datetime.now()
    n = len(A)
    AM = A
    for fd in range(n): 
        for i in range(fd+1,n): 
            if AM[fd][fd] == 0: 
                AM[fd][fd] == 1.0e-18 
            crScaler = AM[i][fd] / AM[fd][fd] 
            for j in range(n): 
                AM[i][j] = AM[i][j] - crScaler * AM[fd][j]
    product = 1.0
    for i in range(n):
        product *= AM[i][i] 
    duration = datetime.datetime.now() - start
    return product,duration.microseconds

print(detfast(losowa(1000,1000,10)))