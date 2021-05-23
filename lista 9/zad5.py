from random import randrange

def losowa(a,b,n):
    matrix=[[randrange(1,n) for i in range(b)] for j in range(a)]
    print(matrix)
    return matrix

def zamAllW(m): 
  for row in m :
    rez = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
  return rez

def zamW(A,i,j): 
    mem = A[i][j]
    A[i][j] = A[j][i]
    A[j][i] = mem
    return A

def przemW(A,i,k):
    a= 'aaa'
    

print(zamW(losowa(5,3,20),2,1))

