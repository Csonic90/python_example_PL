l = list()

for i in range(30):
    l.append((3**i-2**i))
print(l)
print(l.index(1161737179))

l2 = list()
for i in l : 
    l2.append(i%19)
print(l2)

print(10 in l2 , 11 in l2)

num = 0 
while True:
  try:
     num = int(input("podaj liczbe od 1 do 18: "))
  except ValueError:
     print("To nie liczba!")
     continue
  else:
     if num < 1 or num > 18:
            print("Zła liczba!")
            continue
     else :     
        if num in l2 :
            print('liczba wystepuje: ',  l2.count(num), ' razy') 
            break
        else : 
            print('liczba nie występuje') 
            break 


        