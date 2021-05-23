lt1 = {'ala': 'stefan', 'ma': 'cos', 'jakis': 'pies', 'kota': 'i'}

fo = open('p1.txt','w')
ltK = list(lt1.keys())
ltV = list(lt1.values())
    
for i in range(len(lt1)):
    fo.write(ltK[i]+':'+ltV[i]+';') 
     