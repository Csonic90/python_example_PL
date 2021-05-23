sl={'Imię': 'Anna',
    'Wiek':30,
    5:'Costam',
    (6,2):32}

print(sl['Imię'])
print(sl[5])

sl['dodatki']='Costam'

print(sl.keys())
print(sl.values())
print(sl)
del(sl['Wiek'])
print(sl)

l1 = ['lista', 'pierwsza', '1', 'cztery']
l2 = ['2','druga','trzy','ostatni']

dict= {}
for i in range(len(l1)):
    dict[l1[i]] = l2[i]
print(dict)