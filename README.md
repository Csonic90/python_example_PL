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

## Lista 2
### Pętle

## Lista 3
### Pętle II

## Lista 4
### Listy

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