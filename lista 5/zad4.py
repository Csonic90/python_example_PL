lz = list('Alamakota')
print(lz.index('a'))
print(lz.index('m'))
print(lz.index('k'))
# lz.index wyświetla pierwszy znaleziony  index w liście 
# print(lz.index('s')) -błąd nie występuje w liście

l = list()

for i in range(30):
    l.append(str(3**i-2**i))
print(l)
print(l.index('1161737179'))
 