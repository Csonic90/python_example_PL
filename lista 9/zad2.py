A=[[0 for i in range(5)] for j in range(6)]


def zera(a,b) :
    a = [[0 for i in range(a)] for j in range(b)]
    return a 

def id(n) : 
    matrixN = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
      for j in range(n):
         if i==j :
             matrixN[i][j] = 1
    return matrixN

def wyswietlA(a):
    for i in a : 
        print(i)

wyswietlA(id(4))
wyswietlA(zera(5,6))