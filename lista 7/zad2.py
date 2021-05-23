fo = open("p.txt", "r")
s = fo
while s!='' :
    s  = fo.read(3)
    print(s); 

fo.close()