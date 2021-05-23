fo = open("p.txt", "r")
s = fo.read()
ls  = list(s)
element = 'a'
ile = ls.count(element)
print(ile)

fo.close()