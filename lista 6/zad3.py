def zamiana(a):
    temp = a[0]  
    a[0] = a[1] 
    a[1] = temp
    return print(a)
    
a = input('podaj A')
b = input('podaj B')
print(a,b)
l = [a,b]
zamiana(l)
print(l)
