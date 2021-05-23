sl={'kot': 'cat',
    'pies':'dog',
    'komputer':'ccomputer',
    'pociąg':'train'
    }

def bezpow(sl):
     l=list(sl.values())
     if len(l) == len(set(l)): 
         sl2v = list(sl.keys()) 
         sl2k = list(sl.values())
         sl2 ={}
         for i in range(len(sl)):
            sl2[sl2k[i]] = sl2v[i]
         return sl2
     else :
         return 0
print(bezpow(sl))