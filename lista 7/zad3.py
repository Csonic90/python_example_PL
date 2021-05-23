fo = open("p.txt", "a")
a = input('podaj zdanie 1 : ')
b = input('podaj zdanie 2 : ')

fo.write(a+'\n'+ b)

fo.close()