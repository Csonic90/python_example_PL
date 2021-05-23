from math import factorial

print('====zad 3====')
i = 321
s=str(i)
ls=list(s)
print(ls)
print('test 4,5,6')
print(factorial(4))
print(factorial(5))
print(factorial(6))

ln=list(str(factorial(1000)))
nine = '9'
ileNine = ln.count(nine)
print('9 w 1000!')
print(ileNine)

print('0 do 9 w 1000!')
for i in range(9):
    print(ln.count(str(i)))

lm=list(str(factorial(2000)))
print('0 do 9 w 2000!')
for i in range(9):
    print(lm.count(str(i)))