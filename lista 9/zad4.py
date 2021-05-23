from random import randrange

def losowa(a,b,n):
    matrix=[[randrange(1,n) for i in range(b)] for j in range(a)]
    print(matrix)
    return matrix



def mnozenie(A,B):
    colRez = len(A[0])
    rowRez = len(B)
    if len(A[0]) == len(B) :
        rezult = [[ 0 for j in range(len(B[0]))] for i in range(len(A))]
        col = len(rezult)
        row = len(rezult[0])
        for i in range(col): 
            for j in range(row): 
                for k in range(len(B)):             
                     rezult[i][j] += A[i][k] * B[k][j]    
        return rezult
    else: 
        rezult = ['ERROR: matrix : AxB = BxC ' ]
        return rezult
    
print(mnozenie(losowa(3,5,10),losowa(5,4,10)))