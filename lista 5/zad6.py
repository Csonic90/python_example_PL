from math import factorial

l = list()

for i in range(1,100): 
    l.append(1/i)

print('suma: ',sum(l))
print('max: ',max(l))
print('min: ',min(l))

lz=list(str(factorial(1000)))
for i in range(len(lz)):
    lz[i] = int(lz[i])
print('suma liczb 1000!', sum(lz))