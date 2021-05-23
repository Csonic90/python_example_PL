t1=('ala','ma','1','kota')
t2= ('stefan','2','pies','i','kot')

print(t1+t2)
print(t1*2)
print(t2*2)

print(len(t1))
print(max(t1))
print(max(t2))
print(min(t1))

lt1 = list(t1)
for i in range(len(lt1)) : 
    lt1[i] = lt1[i]+" new"
    print(lt1[i])

t1 = tuple(lt1)
print(t1)