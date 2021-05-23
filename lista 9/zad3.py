from random import randrange

def losowa(a,b,n):
    matrix=[[randrange(1,n) for i in range(a)] for j in range(b)]
    print(matrix)
    return matrix

def dodaj(A,B): 
    lenA = [len(A), len(A[0])]
    lenB = [len(B), len(B[0])]
    result=[[0 for i in range(lenA[1])] for j in range(lenA[0])]
    if lenA == lenB :
        result = [[A[i][j] + B[i][j] for j in range(lenA[1])] for i in range(lenA[0])]
        return result
    else : 
        result = ['ERROR: A != B']
        return result

print(dodaj(losowa(3,5,10),losowa(3,4,10)))