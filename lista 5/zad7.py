from math import factorial

lz=list(str(factorial(1000)))
for i in range(len(lz)):
    lz[i] = int(lz[i])


la=list()

for i  in range(len(lz)-1): 
        la.append(str(lz[i])+str(lz[i+1]))
for i in range(10):
    for j in range(10):
        liczba = str(i)+str(j)
        print(liczba ,' - występuje - ', la.count(liczba) ,' razy')


