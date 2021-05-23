# Zadania z programowania Python 

## Spis Zadań 
* [Lista 1 - Zmienne, typy, print, input, if](#lista-1)
* [Lista 2 - Pętle](#lista-2)
* [Lista 3 - Pętle II](#lista-3)
* [Lista 4 - Listy](#lista-4)
* [Lista 5 - Listy II](#lista-5)
* [Lista 6 - funkcje - działadnie na parametrach](#lista-6)
* [Lista 7 - Pliki](#lista-7)
* [Lista 8 - N-tki i Słowniki](#lista-8)
* [Lista 9 - Tabele wielowymiarowe, macierze](#lista-9)

## Lista 1
### Zmienne, typy, print, input, if

(1) Wprowadź do 4 zmiennych a, b, c, d, wartości:
2,5,5.0 oraz 4.2
Wyświetl te zmienne za pomocą polecenia print.
Wyświetl a + b, a + c, a + d i podobnie z ∗ i / zamiast +.
Zinterpretuj wyniki.
(2) Wprowdź do 2 zmiennych s i t wartości:
’kot’ oraz ” i pies”
Wyświetl te zmienne (uwaga: w Pythonie nie ma różnicy między pojedynczym a podwójnym cudzysłowiem).
Wyświetl: s + t, t + s + t oraz 2 ∗ s i zinterpretuj wyniki.
(3) Polecenie input służy do wprowadzania danych z klawiatury.
Stosując składnię typu:
i=input(’Podaj i’)
wprowadź dwie zmienne i oraz j.
Wyświetl i, j oraz i + j. Jak należy zinterpretować wynik?
(wsk. spróbuj wprowadzać różne wartości do i oraz j).
(4) Konwersja w Pythonie pozwala na przekszatałcanie typów (np. zmiennoprzycinkowy 3.14 na całkowity 3, albo alfanumeryczny ’3.14’).
Podstawowe funkcje to int(), float() oraz str(). Powtórz zadanie (3) stosując składnię typu: i=int(input(’Podaj i’))
Jak teraz zinterpretować wyniki?
(5) Napisz program w którym użytkownik wprowadza 2 liczby całkowite.
Przetestuj na tych liczbach operator % (np. a%b lub i%j) dla pary wprowadzanych liczb. Spróbuj odgadnąć znaczenie tego operatora.
(wsk. przetestuj kilka przypadków z drugą liczbą równą 2, potem równą 3..)
Przetestuj w podobny sposób operator // tak aby odgadnąć jego znaczenie.
(6) Napisz program w którym użytkownik wprowadza 3 liczby całkowite.
Następnie, za pomocą polecenia if mają być wyświetlone tylko te z 3 liczb
które są większe od 10. Przetestuj parę razy.
(7) Napisz program w którym użytkownik wprowadza liczbę całkowitą po
czym, za pomocą if, else, ma być wyświetlone czy liczba jest parzysta czy
nieparzyta. Uwaga! Dwie wartości porównujemy za pomocą ==, np. if x==5
(wsk. dla parzystości: zadanie (5))
(8) Rok R jest przestępny jeśli jest podzielny przez 4 z wyjątkiem gdy jest
podzielny przez 100 (wtedy nie jest przestępny), chyba że jest podzielny
przez 400 (wtedy jest przestępny).
Stosując if, elif, else napisz program w którym użytkownik wprowadza rok
i jest wyświetlone czy jest przestępny czy nie.
Przetestuj np. dla: 1900, 1904, 1905, 1600.
(9) Użytkownik wprowadza liczbę zmiennoprzecinkową f (np. f = 93.7415).
Stosując operator % wyświetl cyfry zaraz przed przecinkiem i zaraz po (w
przyładzie: 3 i 7).
(10) Wprowadzone są dwie liczby zmiennoprzecinkowe f i g (np. 2.314 i
65.45). Zamień części całkowite w f i g i wyświetl nowe f i g (w przykładzie
65.314 i 2.45).
(11) Przetestuj, że operator ∗∗ jest potęgowaniem w pythonie. Wprowadzone są dwie liczby i oraz j i program sprawdza która z liczb jest większa
i^j czy j^i i wyświetla odpowedź następująco (na przykładzie i = 3, j = 2):
3 do 2 równe 9 jest większe od 2 do 3 równe 8.
(12) Sprawdź jak za pomocą ∗∗ można liczyć pierwiastki kwadratowe z liczby i ogólnie dowolnego stopnia n.
Oblicz √2, √3 trzeciego stopnia oraz √5 piatego stopnia Która liczba jest największa? Która najmniejsza?

## Lista 2
### Pętle

(1) Przetestuj i zinterpretuj kolejne polecenia:
for i in range(5): print(i)
for i in range(4,8): print(i)
for i in range (1,20,3): print(i)
W którymś z poleceń zamień też print(i) na print(i,end=” ”)
Jaka jest różnica?
(2) Napisz polecenie tak aby wyświetlić:
- w jednym rzędzie liczby parzyste od 2 do 20
- liczby nieparzyste od 19 do 1 (w dół)
- kwadraty liczb od 1 do 10
(3) Napisz program w którym użytkownik wprowadza dwie liczby n i m.
Następnie mają być wyświetlone wszystkie liczby od n do m.
Przykładowo wprowadzająć 2,5 ma wyjść: 2 3 4 5
a wprowadzając 7,3 ma wyjść: 7 6 5 4 3
(4) Napisz program zliczający sumę 1 + 2 + 3 + .. + 99 + 100
Zmodyfikuj go tak aby użytkownik wprowadzał n i program oddawał sumę
1 + 2 + .. + n
(5) Stosując pętlę while znajdź (i wyświetl) najmniejsze n takie, że
1 + 2 + .. + n jest większe od miliona.
(6) Stosując pętlę while znajdź najmniejsze n spełniające:
1 + 1/2 + 1/3 + .. + 1/n > 10
(7) Stosując while napisz program w którym użytkownik wprowadza n i
jest sprawdzane czy n jest kwadratem innej liczby naturalnej (sprawdzamy
1*1, 2*2, itd.)
(8) Napisz program w którym użytkownik wproawdza n po czym jest wyliczone i wyświetlone n! (n silnia) (przetestuj kilka wartości)
(9) Za pomocą pętli (NIE STOSUJĄC potęgowania w pythonie) napisz program w którym użytkownik wprowadza n i m, po czym jest wyliczone i
wyświetlone n do potęgi m. Przetestuj.
(10) Napisz program który dla podanego n zlicza ilość dzielników n, czyli ilość k między 1 a n takich, że k dzieli n.
(11) Użtykownik wprowadza liczbę n. Program wyświetla czy n jest liczbą
pierwszą czy złożoną (wsk. trzeba sprawdzić czy dla jakiegoś k, 2 ¬ k ¬ n−1,

k dzieli n). Przetestuj dla kilku wartości.
(12) Stosując metodę z (11), wyświetl wszystkie liczby pierwsze w zakresie 1-200.

## Lista 3
### Pętle II

(1) Użytkownik wprowadza liczbę n. Program wyświetla czy n jest liczbą
pierwszą czy złożoną (wsk. trzeba sprawdzić czy dla jakiegoś k, 2 ¬ k ¬ n−1,
k dzieli n). Przetestuj dla kilku wartości.
(2) Stosując metodę z (1), wyświetl wszystkie liczby pierwsze w zakresie
1-200.
(3) Za pomocą podwójnej pętli wyświetl kwadrat składający się z gwiazdek (*) o rozmiarze 10 na 10.
(4) Zmodyfikuj (3) tak aby wyświetlić sam brzeg kwadratu. (W warunkach
dla if można stosować operatory logiczne and oraz or).
(5) Zmodyfikuj (3) aby wyświetlić brzeg kwadratu z jedną przekątną. Następnie ma być wyświetlony brzeg z obiema przekątnymi.
(6) Zmodyfikuj (3) aby wyświetlić szachownicę gwiazdek (wsk. może być
przydatna pewna parzystość).
(7) Wyświetl tabliczkę mnożenia do 10. Zrób to etapami: najpierw sama
zawartość tabliczki (100 liczb w 10 wierszach rozdzielonych spacjami). Tu
może wyjść trochę krzywo wtedy zastanów się jak to poprawić. Na koniec
dodaj wiersz liczb od 1 do 10 nad tabliczką i podobną kolumnę na lewo od
niej aby uzyskać czytelną tabliczkę mnożenia.
(8) Zmodyfikuj (3) tak aby wyświetlić po koleji 4 trójkąty prostokątne gwiazdek (pełne - z gwiazdkami w środku) z kątami prostymi w 4 rogach kwadratu
z (3).
(9) Zmodyfikuj tabliczkę możenia z (7) tak aby zamiast iloczynu liczb a
(wiersz) i b (kolumna) był znak >, < lub = w zależności od tego czy a
b > ba
(w pythonie potęgowanie: **), < czy równe.
(10) (Dodatkowe) Zmodyfikuj 1 tak aby utworzyć z gwiazdek (w przybliżeniu):
- koło wypełnione gwiazdkami
- okrąg, czyli brzeg poprzedniego (oczywiście przybliżony)

## Lista 4
### Listy

(1) Stwórz listę 4-elementową l zawierającą po kolei:
3,’alfa’,2.71,’kot’
Za pomocą print zinterpretuj l[i] dla i całkowitych (ujemnych też).
Dla których i nie będzie błędu?
Zmień pierwszy element listy na 4, a ostatani na ’pies’ i wyświetl listę l.
Skopiuj listę l do listy l2. Wyświetl l oraz l2. Zmodyfikuj pierwszy element
l2 i wyświetl obie listy. Co można zauważyć? (nie stworzyliśmy nowej listy
tylko stworzyliśmy nowy odnośnik-reference do starej listy.)
Skopiuj teraz l do l3 za pomocą: l3=l.copy()
Zmień pierwszy element l3 i wyświetl listy l i l3. Co można zauważyć?
(2) Dwie listy można połączyć (konkatenacja) za pomocą +, np. aby dodać element 6.4 do listy l stosujemy składnię:
l = l + [6.4] ([6.4] jest listą 1-elementową)
Pustą listę można zdefiniować przez:
l=[]
Stwórz (za pomocą pętli) listę 10-elementową kwadratów: 1, 4, 9, .., 100
Wyświetl listę (print). Następnie zmień znak elementów parzystych listy i
wyświetl taką zmienioną listę.
(3) Napisz program w którym użytkownik najpierw podaje ilość liczb n
do wpisania. Następnie n liczb jest wpisywane do listy. Wreszcie program
ma znaleźć i wyświetlić największą i najmniejszą z tych liczb.
(4) Użytkownik wprowadza n. Stoworzona jest n-elementowa lista zawierająca:
sin(1), sin(2), ..., sin(n).
Wreszcie program znajduje i wyświetla największy i najmniejszy element
tablicy. Przetestuj z coraz większymi n. Co się dzieje z elementami największym i najmniejszym?
(5) Polecenie del służy do usuwania elementów listy, składnia:
del lista[5] (usuwa 6-sty element listy lista)
Stwórz listę składającą się z liczb od 100 do 150.
Następnie usuń z listy elementy z liczbami 105, 110, 115,..,140, 145 i wyświetl końcową listę.
Jeśli końcowa lista jest inna niż oczekujemy zastanów się dlaczego i zmodyfikuj program.
(6) Stwórz 10-elementową listę l zawierającą różne liczby całkowite. Następnie (jak najprościej) utwórz listy (pamiętaj o kopiowaniu z l.copy() patrz
1
2
(1)):
l2, w której początkowy element listy jest przeniesiony na koniec.
l3, końcowy element listy jest przeniesiony na początek.
l4, odwrócona lista l.
l5, lista składająca się tylko z parzystych elementów l.
l6, lista składająca się z nieparzystych elementów l o indeksach parzystych
Sprawdź wyświetlając wszystkie te listy.
(7) Liczba π znajduje się w module math, jako pi. Napisz program który wpisuje kolejne 50 cyfr rozwinięcia pi do listy. Wreszcie wyświetl tą listę.


## lista 5 
### Listy II

(1) Niech s=’Ala ma kota’. Przekształć s w listę ls za pomocą konwersji
lz = list(s). Wyświetl lz.
Chcemy teraz wyświetlić w pętli każdy element listy na dwa sposoby. Funckją len uzyskujemy długość listy: len(lz). Dokończ polecenie:
for i in range(len(lz)): .....
Drugi sposób jest taki, że i jest równe kolejnym elementom listy. Dokończ:
for i in lz: ......

(2) Zachowujemy lz z (1). Metoda count zwraca ilość występowania danego elementu w liście. Przykładowa składnia: ile=lista.count(element).
Zlicz ilość ’a’ w liście lz.
Napisz teraz program gdzie wprowadzone jest zdanie s. Następnie s jest
zmienione na listę ls i wyświetlona jest ilość literek a w s.

(3) Niech i będzie liczbą całkowitą. Np. i = 321. Spróbuj zamienić i na
listę (jaki jest błąd?). Aby uzyskać listę cyfr i, najpierw zamieniamy i na
ciąg znaków, s = str(i). Potem tworzymy listę jak w poprzednich zadaniach.
Sprawdź że f actorial wgrana z math (from math import factorial) jest silnią
(np. przetestuj dla 4, 5, 6).
Niech n = 1000!. Zrób z n listę i za pomocą count oblicz ile jest cyfr 9 w n.
Wreszczie zrób to samo dla wszystkich cyfr od 0 do 9. Co można zauważyć?
Zmień 1000! na 2000! i sprawdź ilość każdej z cyfr jeszcze raz.

(4) Niech lz = list('Alamakota'). Wyświetl lz.index('a'), lz.index('m'),
oraz lz.index('k') i zinterpretuj uzyskane wartości. (co jest zwracane jeśli
element występuje wiele razy?)
Przetesuj lz.index('s'), skąd błąd?
Zamiast l = l + [element] można stosować l.append(element).
Stwórz listę l składającą się z liczb postaci 3n−2
n dla n od 0 do 30. Wyświetl
na jakiej pozycji znajduje się liczba 1161737179. Potwierdź to obliczając i
wyświetlając 3^n − 2^n dla odpowiedniego n.

(5) Widzieliśmy że index generuje błąd jeśli elementu nie ma w liście. Aby
tego uniknąć, możemy sprawdzić czy element jest w liście za pomocą in.
Niech l będzie listą z (4). Stwórz za pomocą pętli listę l2 z elementami:
reszty z dzielenia przez 19 elementów z l.
Wyświetl 10 in l2 oraz 11 in l2. Co uzyskujemy?
Użytkownik wpowadza liczbę n (między 0 a 18). Następnie ma być wyświetlone:
nie ma tej liczby w l2 (lub) ta liczba występuje w l2 (tyle) razy.

(6) Stwórz listę l składającą się z ułamków 1, 1/2, 1/3...,1/100. Wyświetl i
zinterpretuj sum(l), min(l), max(l).
Stwórz listę lz cyfr 1000! jak w (3). Zrób z niej listę liczb całkowitych (konwersję int(...) należy zastosować na każdym elemencie z osobna). Wreszcie
oblicz sumę cyfr 1000!

(7) Znajdź wszystkie pary cyfr występujące w 1000! Przedstaw wynik jako:
00 - występuje ... razy
01 - występuje ... razy
...
99 - występuje ... razy

## lista 6 
### funkcje - działadnie na parametrach

(1) Aby zamienić zawartość 2 zmiennych (np. a i b) trzeba się posłużyć
zmienną pomocniczą c wpisując w nią tymczasowo wartość np. a. Napisz
program z ustalonymi zmiennymi całkowitymi a i b. Wyświetl a i b, zamień
ich zawartość i wyświetl nowe a i b.

(2) Spróbuj napisać funkcję zmien(a, b) która ma zamienić zawartość wprowadzonych parametrów. Wyświetl zamienione zmienne WEWNĄTRZ funkcji i PO ZASTOSOWANIU funkcji. Czy udało się zamienić parametry?

(3) Spróbuj powtórzyć (2) przekazując do funkcji zamien listę 2-elementową.
Wyświetl, po zamianie, listę wewnątrz funkcji i na zewnątrz. Czy udało się
zamienić elementy listy?

(4) Napisz funkcję odwroc(lista), która odwraca listę, np:
l = [1, 5, 4, 3] i po zastosowaniu funkcji l = [3, 4, 5, 1]. Sprawdź czy funkcja
działa.

(5) (Sortowanie bąbelkowe) Napisz funkcję sortuj(lista) która porządkuje listę lista rosnąco. Przetestuj tworząć listę 10-elementową liczb losowych
z zakresu [1..100].
Stwórz teraz listę kilkuelementową składającą się ze słów. Zastosuj na niej
funkcję sortuj i wyświetl na nowo listę. Co się stało? Przeanalizuj dlaczego.

(6) Stosując sortuj z poprzedniego zadania, napisz program w którym użytkownik wprowadza do zmiennej jakieś zdanie składające się ze słów i spacji.
Następnie ma być wyświetlone zdanie składjące się z tych samych słów ale
posortowanych alfabetycznie. Wreszcie ma być wyświetlone zdanie składające się z tych samych słów w kolejności od najkrótszych do najdłuższych
(jeśli słowa są tej samej długości nie jest ważne w jakiej kolejności są wyświetlane).
Np. dla ’Dzisiaj jest bardzo piękna pogoda’ na wyjść: bardzo Dzisiaj jest
piękna pogoda
jest bradzo piękna pogoda Dzisiaj

(7) (DODATKOWE) Stosując funkcje ord i chr wygeneruj listę składającą
się ze 100 ’losowych’ słów (od 3 do 8 liter). Posortuj uzyskaną listę alfabetycznie.
Zmień generowanie listy, tak aby conajmniej co 3 litery pojawiała się samogłoska i tak aby słowa nie zawierały podwójnych liter (obok siebie), czyli
nie chcemy np. appot (dwa razy p) ale apotp jest w porządku. Posortuj taką
listę alfabetycznie.

## lista 7 
### Pliki

(1) Operacje na plikach są możliwe dzięki obiektom plikowym, np:
fo = open(’plik.txt’,’w’)
TU COŚ WPISUJEMY DO PLIKU
fo.close()
Podstawowe parametry przy otwieraniu pliku (są jeszcze inne opcje):
’w’ (write) plik jest stworzony i można w nim coś zapisywać (jeśli istnieje to
poprzednia zawartość zostanie wymazana)
’r’ (read) czytamy z istniejącego pliku bez modyfikacji
’a’ (append) do istniejącego pliku dopisujemy nowe dane
Do pliku (otworzonego z ’w’ lub ’a’) wpisujemy dane:
fo.write(’To zostanie do dane do pliku!\nTo będzie w nowej linijce\n’)
Stwórz plik o nazwie p.txt i wpisz do niego trzy dowolne linijki.
Sprawdź że plik powstał otwierając p.txt w edytorze (np. klikając na p.txt)
Zmodyfikuj wpisane linijki, uruchom program i sprawdź ponownie zawartość
p.txt.

(2) Otwórz plik p.txt (stworzony w (1)) do odczytu (opcja ’r’).
Przetestuj: s=fo.read(5); print(s); s=fo.read(3); print(s); s=fo.read(); print(s)
Gdy dojdziemy do końca pliku s przyjmuje wartość ” (pusty łańcuch).
Polecenie break powoduje wyjście z pętli while lub for. Stosując while 1:
(nieskończona pętla, bo 1 odpowiada prawdzie) napisz program odczytujący
i wyświetlający po 3 znaki z pliku p.txt. Trzeba użyć break gdy s jest równe
”.

(3) Otwórz plik p.txt do dodawania (opcja ’a’). Za pomocą dwukrotnego
input po wywołaniu programu użytkownik ma dodać 2 linijki do pliku. Przetestuj i sprawdź nową zawratość pliku p.txt. Jeśli linijki się sklejają należy
dodać na konću każdej linijki ’\n’ (skok do następnej linijki). Przetestuj.

(4) Napisz program który zlicza ilość literek ’a’ w pliku p.txt. Przetestuj
zmieniając w edytorze ilość ’a’ w tym pliku.

(5) Napisz program który sprawdza czy wprowadzone słowo za pomocą
input znajduje się w pliku i wyświetla linijkę pliku z tym słowem. Można użyć fo.readline() do pobierania całych linijek. Przydatne może też być
polecenie in dla łańcucha znaków.

(6) Napisz program który otwiera plik p.txt do odczytu i tworzy plik p2.txt
który ma być taki jak p.txt oprócz tego że spacje mają być zamienione na
gwiazdki (*). Przetestuj.

(7) (Dodatkowe) Takie jak 6 ale w pliku p2.txt małe litery z p.txt mają
być zamienione na duże litery. Przetestuj.

## lista 8  
### N-tki i Słowniki

(1) N-tki (tuples) są stałymi listami. W ich definicji stosujemy nawiasy okrągłe zamiast kwadratowych. Np.:
ntka=(1,’alfa’,5,3.14) określa 4 elementową n-tkę. Dostęp do poszczególnych
elementów uzyskujemy tak jak dla list poprzez:
print(ntka[0], ntka[3], nttka[-2]) co wyświetli pierwszy, czwarty i drugi od
końca element n-tki ntka.
Można przechodzić pomiędzy ntkami a listami i na odwrót ta pomocą l=list(t)
oraz t=tuple(l). Zdefiniuj ntki t1 i t2 z kilkoma elementami. Przetestuj na
nich operacje i funkcje: +, *2, len, max
Spróbuj zmienić pojedynczy element ntki t1. Jak się nie da, zrób to przechodząc przez listę l, usuwając t1 (polecenie del) i przepisując l do nowego
t1. Sprawdź za pomocą print.

(2) Słowniki przypominają listy, ale zamiast indeksowania liczbami naturalnymi 0,1,2... można indeksować dowolnymi stałymi elementami w pythonie
(czyli liczbami, łańcuchami, n-tkami). Przykładowa składnia:
sl={’Imię’: Anna, ’Wiek’:30, 5:’Costam’, (6,2):32}
Takie sl ma 4 indeksy (’Imię’, ’Wiek’, 5, (6,2)) za pomocą których możemy
otrzymać zawartości: sl[’Imię’], sl[5] itd.
Nowe pole możemy dodawać przez:
sl[’dodatki’]=’Costam’
Przetestuj za pomocą print: sl.keys(), sl.values() i sl.
Aby usunąć element sl: del sl[’Wiek’]
Stwórz 2 listy tej samej długości l1 i l2 bez powtarzających się elementów
w l1. Za pomocą pętli for stwórz słownik dict (przed pętlą pusty dict={})
którego indeksy są w l1 a wartości w l2. Sprawdź za pomocą print.

(3) Napisz funkcję bezpowt(sl) która pobiera jako parametr słownik, sprawdza czy wśród jego wartości jakieś elementy są takie same czy nie i zwraca
1 (jeśli nie ma powtórzeń) lub 0 (jeśli są). Przetestuj na dwóch słownikach, jednym z powtórzeniami, a drugim bez. Wsk.: może być pomocna
lista l=list(sl.values())

(4) Stosując funkcję z (3) napisz funkcję odwr(sl) która ma sprawdzić czy
nie ma powtórzeń wśród wartości sl i jeśli ich nie ma tworzy i zwraca słownik
sl2 w którym indeksy i wartości są zamienione. Jeśli są powtórzenia funkcja
wyświetla komunikat o błędzie.
Przetestuj tworząć kilkuelementowy słownik polsko-angielski. Funkcja powinna stworzyć z niego słownik angielsko-polski.

(5) Stwórz krótki słownik sl z indeksami i wartościami łańcuchy znaków, np.
taki jak w (4). Następnie wygeneruj plik zawierający klucz:wartość;klucz:wartość;itd..
Np. jeśli sl[’kot’]=’cat’, to plik może się zaczynać od: kot:cat;
Sprawdź czy plik został poprawnie stworzony.

(6) Korzystając z pliku wygenerowanego w (5) odtwórz słownik sl.


## lista 9 
### Tabele wielowymiarowe, macierze

(1) W pythonie dopuszczalne są listy zawierające listy, np.:
A=[[1,2],[3,4]]
stworzy listę skłdającą się z 2 list 2-elementowych. Poszczególne elementy
uzyskamy składnią A[i][j]. W ten sposób uzyskaliśmy tablicę 2 na 2. Stwórz
takie A, wyświetl je za pomocą print oraz jako macierz (wiersz po wierszu).

(2) Aby stworzyć większe tabele wygodnie jest stosować składnię typu:
A=[[0 for i in range(5)] for j in range(6)]
co stworzy macierz 6 (wierszy) na 5 (kolumn) wypełnioną zerami. Następnie można zmieniać wartości A (bez stworzenia A nie dałoby się stosować
przykładowo A[3][4]=7).
Napisz funkcję zera(a, b) która zwraca macierz rozmiaru a na b wypełnioną
zerami oraz funkcję id(n) która zwraca macierz jednostkową n na n (jedynki
na przekątnej, poza przekątną zera). Wreszczie napisz funkcję wyswietl(A)
która wyświetla macierz A wiersz po wierszu (dla rozmiaru macierzy przyda
się funkcja len). Przetestuj czy wszystkie funkcje działają.

(3) Napisz funkcję losowa(a, b, n) która zwraca macierz rozmiaru a na b
wypełnioną losowymi liczbami naturalnymi z zakresu od 1 do n. Napisz
funkcję dodaj(A, B) która zwraca sumę macierzy A i B (i zwraca pustą listę
jeśli wymiary A i B nie są takie same).
Przetestuj tworząc macierze A i B rozmiaru 2 na 3 wypełnione losowymi
liczbami z zakresu od 1 do 10. Wyświetl A, B dodaj je i wyświetl ich sumę.

(4) Do zadania (3) dopisz funkcję pomnoz(A, B) która zwraca iloczyn macierzy A i B (lub pustą listę jeśli wymiary A i B nie pozwalają na przemnożenie
macierzy). Przetestuj na dwóch macierzach 2 na 2.

(5) Napisz funkcje dla operacji elementarnych na wierszach macierzy:
zamW(A, i, j) zwraca macierz uzyskaną z A po zamianie i-tego i j-tego wiersza.
przemW(A, i, k) zwraca macierz gdzie i-ty wiersz A jest przemnożony przez
k.
dodajW(A, i, j, k) zwraca macierz gdzie do i-tego wiersza dodany jest k razy
j-ty wiersz.
Przetestuj te funkcje na przykładowej macierzy.

(6) Napisz funkcję det(A) zwracającą wyznacznik macierzy A w sposób rekurencyjny. Przetestuj szybkość dla coraz większych macierzy kwadratowych
tworzonych np. za pomocą losowa z (3).