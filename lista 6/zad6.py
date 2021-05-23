from random import randint

x = input('napisz zdanie')
lZdanie = x.split(' ')

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
    return print(' '.join(lista))

def sortowanieLenghtBombelkowe(lista):
    n = len(lista)
    while n > 1:
        zamien = False
        for l in range(0, n-1):
            if len(lista[l]) > len(lista[l+1]):
                lista[l], lista[l+1] = lista[l+1], lista[l]
                zamien = True  
        n -= 1
        if zamien == False: break
    return print(' '.join(lista))
print(lZdanie)  

sortowanieBabelkowe(lZdanie)
sortowanieLenghtBombelkowe(lZdanie)
