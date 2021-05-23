sl={'Imię': 'Anna',
    'Wiek':30,
    5:'Costam',
    (6,2):32,
    }
sl2={'Imię': 'Anna',
    'Wiek':30,
    5:'Costam',
    (6,2):32,
    'ala':'Costam'}

def bezpow(sl):
     l=list(sl.values())
     if len(l) == len(set(l)): 
         return 1
     else :
         return 0
print(bezpow(sl))
print(bezpow(sl2))