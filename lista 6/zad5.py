from random import randint

lRandom = [randint(1,100) for i in range(10)]
lString = ['zzz','aaa','bvbb','ssss','rrrr']
def sortowanieBabelkowe(lista):
    n = len(lista)
    while n > 1:
        zamien = False
        for l in range(0, n-1):
            if lista[l] > lista[l+1]:
                lista[l], lista[l+1] = lista[l+1], lista[l]
                zamien = True  
        n -= 1
        if zamien == False: break
        
    return print(lista)
print(lRandom)        
sortowanieBabelkowe(lRandom)
print(lString)
sortowanieBabelkowe(lString)