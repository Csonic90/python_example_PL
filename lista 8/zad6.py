fo =  open('p1.txt','r') 
rfo = fo.read()
t = {}
splitRFo  = rfo.split(';')
for i in range(len(splitRFo)-1):
    getItem = splitRFo[i].split(':')
    tK = getItem[0]
    tV = getItem[1]
    t[tK] = tV
fo.close()
print(t)
