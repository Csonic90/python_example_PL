fo = open("p.txt", "r")
s = fo.read()
ls  = list(s.split())
element = input('podaj szukane słowo')
iloscElem = ls.count(element)
if iloscElem > 0 :
    print('słowo "'
    + element 
    +'" znajduje sie w szukanym tekscie : '
    + str(iloscElem)+' razy' )
else : 
    print('slowo nie występujeala')

fo.close()