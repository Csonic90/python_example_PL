fin = open("p.txt", "r")
fout = open("p2.txt", "w")

s = fin.read()
ls  = s.replace(' ', '*')
fout.write(ls)

fin.close()
fout.close()
