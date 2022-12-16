#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
zad. 2
Stwórz zmienną o nazwie `PI` i wartości 3.14. Wykorzystaj ją do obliczenia pola koła o promieniu 12.
Wynik wyświetl na ekran.
"""
pi = 3.14
r = 12
A = pi * r ** 2
print(A)

"""
zad. 3
 * Stwórz dwie zmienne imie i nazwisko i przypisz do dowolne wartości (nie muszą być prawdziwe).
 * Wypisz obie zmienne na ekran.
 * Połącz obie zmienne spacją i wynik zapisz do zmiennej dane.
"""
imie = 'Agata'
nazwisko = 'Radzikowska'

print(f'Nazywam się {imie} {nazwisko}.')

dane = imie + ' ' + nazwisko
print(dane)

"""
zad. 4
Przekonwertuj wartość b na int, a następnie oblicz średnią z a, b i c.
"""
a = 314
b = "500"
c = 4.5

mean = (a + int(b) + c)/3
print(mean)

"""
zad. 6
Stwórz 3 elementową listę, która zawiera nazwy 3 Twoich ulubionych owoców.
Wynik przypisz do zmiennej `owoce`.
"""
owoce = ['banan','truskawka','ananas']
print(owoce)

"""
zad. 7
Dodaj do powyższej listy jako nowy element "pomidor".
"""
owoce.append('pomidor')
print(owoce)

"""
zad. 8
Usuń z powyższej listy drugi element.
"""
del owoce[1]
print(owoce)

"""
zad. 9
Rozszerz listę o tablice ['Jabłko', "Gruszka"].
"""
owoce += ['Jabłko', "Gruszka"]
print(owoce)

"""
zad. 10
Wyświetl listę owoce, ale bez pierwszego i ostatniego elementu.
"""
print(owoce[1:-1])

"""
zad. 11
Wyświetl co trzeci element z listy owoce.
"""
print(owoce[0:4:3])

"""
zad. 7
Stwórz pusty słownik i przypisz go do zmiennej magazyn.
"""
magazyn = {}

"""
zad. 8
Dodaj do słownika magazyn owoce z listy owoce, tak, aby owoce były kluczami,
zaś wartościami były równe 5.
"""
magazyn = {x:5 for x in owoce}
print(magazyn)

"""
zad. 9
 * Stwórz listę składającą się z parzystych elementów listy l (l. parzystych)
 * Stwórz listę z elementów l o nieparzystych indeksach
"""
l = [4, 5, 8, 9, 0, 3]
l_parzyste = []
l_nieparzyste = []

for x in l:
    if x % 2 == 0:
        l_parzyste.append(x)
    else:
        l_nieparzyste.append(x)

print(l_parzyste)
print(l_nieparzyste)

"""
zad. 10
Lista `zad10` zawiera 2 elementy - listy. Stwórz nową listę `zad10_flat`,
która będzie składać się z elementów każdej z tych listy.
"""
zad10 = [[9, 8, 12, 7], [12, 33, 8, 7]]
zad10_flat = zad10[0] + zad10[1]
print(zad10_flat)

"""
zad. 11
Stwórz listę zad11out, która powstanie z <zad11> poprzez usunięcie 
powtarzających się wartości.
"""
zad11 = [3, 2, 2, 6, 9, 10, 1, 3]
zad11out = list(set(zad11))
print(zad11out)

"""
zad. 12
Wyświetl sumę liczb od 1 do 256.
"""
suma = 0
for x in range(257):
    suma += x
print(suma)

# shorter version:
suma = sum([x for x in range(257) ])
print(suma)

"""
zad. 13
Wyświetl sumę liczb parzystych od 1 do 256.
"""
suma = 0
for x in range(257):
    if x % 2 ==0:
        suma += x
print(suma)

# shorter version:
suma = sum([x for x in range(257) if x % 2 == 0])
print(suma)

"""
zad. 14
Poniżej znajdują się 2 słowniki z danymi o liczbie przejazdów rowerami miejskimi w Montrealu w 2018 z podziałem na miesiące.
Pierwszy słownik zawiera informacje o przejazdach wykonanych przez posiadaczy abonamentu, a drugi przez ludzi, który
nie mają wykupionego abonamentu. Dane pochodzą ze strony https://montreal.bixi.com/en/open-data. 

a) Stwórz trzeci słownik `all_rides`, w którym zliczysz łączną liczbę przejazdów w każdym z miesięcy.
b) Wykorzystując listę `months` wyświetl ile w danym miesiącu odbyło się przejazdów. Załóż, że odbyło się 0 przejazdów 
w miesiącach, którycj brakuje w `all_rides`.
c) Oblicz jaki procent stanowią w ciągu roku przejazdy okazjonalne.
d) Czy obie grupy osiągają największą liczbę przejazdów w tym samym miesiącu? Spróbuj znaleźć odpowiedź bez patrzenia
na wartości w podanych słownikach.
"""

members = {'April': 211819, 'May': 682758, 'June': 737011, 'July': 779511, 'August': 673790,
           'September': 673790, 'October': 444177, 'November': 136791}

occasionals = {'April': 32058, 'May': 147898, 'June': 171494, 'July': 194316, 'August': 206809,
               'September': 140492, 'October': 53596, 'November': 10516}

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December']

#a) Stwórz trzeci słownik `all_rides`, w którym zliczysz łączną liczbę przejazdów w każdym z miesięcy.
#a1 >> tylko jeżeli liczby i nazwy miesięcy w obu słownikach są takie same:

all_rides = {}

for month, rides in members.items():
    all_rides[month] = rides + occasionals[month]

print(all_rides)

#a >> dla dowolnych misięcy w occasionals i members:

all_rides2 = {}

for month in months:

    if month in members.keys() and month in occasionals.keys():
        all_rides2[month] = members[month] + occasionals[month]

    if month in members.keys() and month not in occasionals.keys():
        all_rides2[month] = members[month]

    if month not in members.keys() and month in occasionals.keys():
        all_rides2[month] = occasionals[month]
    else:
        pass

print(all_rides2)

#b) Wykorzystując listę `months` wyświetl ile w danym miesiącu odbyło się przejazdów. Załóż, że odbyło się 0 przejazdów
# w miesiącach, którycj brakuje w `all_rides`.

all_rides3 = {month:0 for month in months}
print(all_rides3)

for month in months:

    if month in members.keys() and month in occasionals.keys():
        all_rides3[month] = members[month] + occasionals[month]

    if month in members.keys() and month not in occasionals.keys():
        all_rides3[month] = members[month]

    if month not in members.keys() and month in occasionals.keys():
        all_rides3[month] = occasionals[month]
    else:
        pass

print(all_rides3)

#c) Oblicz jaki procent stanowią w ciągu roku przejazdy okazjonalne.

occasionals_all = sum(list(occasionals.values()))
all_rides_all = sum(list(all_rides3.values()))

percent = (occasionals_all/all_rides_all)
print(f'{round(percent*100,2)}%')


"""
zad. 15
 * Stwórz listę składającą się z dowolnych 100 elementów, np. może być
 to listę kwadratów liczb.
 * Sprawdź za pomocą funkcji len liczbę elementów tej listy.
 * Usuń trzeci, element.
 * Usuń przedostatni element.
 * Wyświetl pierwsze 10 elementów.
"""
lista = [x for x in range(100)]
print(lista)

# Sprawdź za pomocą funkcji len liczbę elementów tej listy.
print(len(lista))

# Usuń trzeci element.
del lista[2]
print(len(lista))

# Usuń przedostatni element.
del lista[-2]
print(len(lista))

# Wyświetl pierwsze 10 elementów.
print(lista[0:10])

"""
zad. 16
Znajdz najmniejsz element w poniższej liście.
"""
numbers = [0, 6, 9, -10, -5, 9, 8, -6]
print(min(numbers))

"""
zad. 17
Wyświetl poniższy słownik, tak, aby każda para "klucz: wartość"
była w osobnej linii.
"""
s = {'Tomasz': [3, 4, 5, 4], 'Agata': [5, 5, 5, 4]}
for item in s.items():
    print(item)

"""
zad. 18
Poniżej jest podana lista liczby. Stwórz słownik <counter>, którego kluczami
będą wartości występujące w liście <liczby>, a wartościami ile dany element
wystąpił w liście <liczby>.
"""
liczby = [3, 4, 3, 3, 4, 7, 9]

counter = {x:liczby.count(x) for x in liczby}
print(counter)

"""
zad. 19
Poniższy słownik oceny dwóch osób. Stwórz nowy słownik z takimi samymi kluczami,
ale wartościami tego słownika będą średnie oceń.
"""
s = {'Tomasz': [3, 4, 5, 4], 'Agata': [5, 5, 5, 4]}
import statistics as st

srednie = {x:st.mean(s[x]) for x in s}
print(srednie)

"""
zad. 20
Dla podanego poniżej słownika S, stwórz nowy słownik, którego kluczami będą
wartości słownika S, a wartościami: odpowiadające im klucze z S.
"""
s = {'Klucz1': 'Wartosc1', 'Klucz2': 'Wartosc2', 'Klucz3': 'Wartosc3'}
S = {}
for key, value in s.items():
    S[value] = key
print(S)

"""
zad. 21
Napisz kod, który wypisze na ekran elementy, które występnują w obu poniżej podanych funkcjach.
"""
l1 = [99, 8, 7, 55]
l2 = [55, 111, 11, 99, 8]

l_wspolne = []
for x in l1:
    if x in l2:
        l_wspolne.append(x)
print(l_wspolne)

"""
zad. 22
Napisz kod, który znajdzie najdroższy produkt  w poniższym słowniku.
"""
zakupy = {'telefon': 1000, 'ładowarka': 35, 'chleb': 4.30, 'kawa': 55, 'gramofon': 240}
print((list(zakupy.keys()))[(list(zakupy.values())).index(max(zakupy.values()))])

"""
zad. 23
Stwórz listę składającą się z wartości słownika zakupy.
"""
zakupy = {'telefon': 1000, 'ładowarka': 35, 'chleb': 4.30, 'kawa': 55, 'gramofon': 240}

lista2 = list(zakupy.values())
print(lista2)

"""
zad. 24
Wyświetl na ekranie poniższy wzór:
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
"""
print(f"*\n**\n***\n****\n*****\n****\n***\n**\n*")


"""
1. Napisz funckję, która zamieni stopnie Fahrenheita na Celcjusza zgodnie ze
wzorem:
    F = 32 + 9/5*C
Następnie dodaj kowałek kodu, który pozwoli na wczytanie temperatury z
klawiatury, a następnie wyświetli temperaturę w Fahrenheitach.
"""
def fah(x,y):
    if y.upper() == 'C':
        temp =  32 + 9/5 * x
        result = print(f'{x} {y.upper()} to {temp} F.')
    if y.upper() == 'F':
        temp = (x - 32) * 5/9
        result = print(f'{x} {y.upper()} to {temp} C.')
    return(result)

fah(100,'c')


"""
2. Poniższa słownik Letters zawiera informacje o literach w grze Scrubble, dokładniej ile tabliczek z daną literą występuje w grze
oraz wartość punktową danej litery.

Napisz program, który wczyta z klawiatury słowo, a nastęnie zwróci ile dane słowo jest warte punktów.
"""
Letters = {
        'a': { 'quantity' : 9, 'value': 1},
        'b': { 'quantity' : 2, 'value': 3},
        'c': { 'quantity' : 2, 'value': 3},
        'd': { 'quantity' : 4, 'value': 2},
        'e': { 'quantity' : 12, 'value': 1},
        'f': { 'quantity' : 2, 'value': 4},
        'g': { 'quantity' : 3, 'value': 2},
        'h': { 'quantity' : 2, 'value': 4},
        'i': { 'quantity' : 9, 'value': 1},
        'j': { 'quantity' : 1, 'value': 8},
        'k': { 'quantity' : 1, 'value': 5},
        'l': { 'quantity' : 4, 'value': 1},
        'm': { 'quantity' : 2, 'value': 3},
        'n': { 'quantity' : 6, 'value': 1},
        'o': { 'quantity' : 8, 'value': 1},
        'p': { 'quantity' : 2, 'value': 3},
        'q': { 'quantity' : 1, 'value': 10},
        'r': { 'quantity' : 6, 'value': 1},
        's': { 'quantity' : 4, 'value': 1},
        't': { 'quantity' : 6, 'value': 1},
        'u': { 'quantity' : 4, 'value': 1},
        'v': { 'quantity' : 2, 'value': 4},
        'w': { 'quantity' : 2, 'value': 4},
        'x': { 'quantity' : 1, 'value': 8},
        'y': { 'quantity' : 2, 'value': 4},
        'z': { 'quantity' : 1, 'value': 10},
        '*': { 'quantity' : 2, 'value': 0}
        }
print(Letters['k']['value'])
def scrabble(str):
    scr_lista = []
    for x in str:
        scr_lista.append(Letters[x.lower()]['value'])
    wartosc = sum(scr_lista)
    return(print(wartosc))

scrabble('AgaXYSXXXdsD')

"""
3. Oblicz ile wynosi suma wszystkich punktów na wszystkich kostkach w grze Scrabble.
"""
wartosc2 = 0
for key, value in Letters.items():
    wartosc2 += (value['quantity']*value['value'])
print(wartosc2)

"""
4. Korzystając z funkcji `permutations` z biblioteki `itertools` wypisz wszystkie
możliwe "słowa", które można ułożyć z liter z tablicy tiles.
"""

tiles = ['c','o','n','t']

def perm(lista):
    result = []
    lista_slowo = ''.join(lista)
    p = permutations(lista_slowo)

    for x in p:
        result.append(x)

    return(print(result))

perm(tiles)

"""
5. Napisz program, który wskaże, czy który gracz wygrał (Albo jest remis) w
poniższych grach "kołko i krzyżyk". Spacja oznacza wolne pole, które jeszcze
nie zostało zajęte.
"""

board_1 = [['x', 'x', ' '],
           ['x', 'o', ' '],
           ['x', 'o', 'o']]

board_2 = [['o', 'x', ' '],
           ['x', 'o', ' '],
           ['x', 'o', 'o']]

board_3 = [[' ', 'o', ' '],
           ['x', 'o', ' '],
           ['x', 'o', 'o']]

board_4 = [['o', 'x', ' '],
           ['x', 'o', ' '],
           ['x', 'o', 'x']]

board_5 = [['o', 'x', ' '],
           ['x', 'o', ' '],
           ['x', 'o', ' ']]

print(board_5[0][0])

print(board_5[0][0] != ' ')



def tictactoe_check(board):

    # poziome (x3):
    if board[0][0] != ' ' and (board[0][0] == board[0][1] and board[0][1] == board[0][2]):
        result = print(f'{board[0][0]} wygral!')
        return (result)

    if board[1][0] != ' ' and (board[1][0] == board[1][1] and board[1][1] == board[1][2]):
        result = print(f'{board[1][0]} wygral!')
        return (result)

    if board[2][0] != ' ' and (board[2][0] == board[2][1] and board[2][1] == board[2][2]):
        result = print(f'{board[2][0]} wygral!')
        return (result)


    # pionowe (x3):
    if board[0][0] != ' ' and (board[0][0] == board[1][0] and board[1][0] == board[2][0]):
        result = print(f'{board[0][0]} wygral!')
        return (result)

    if board[0][1] != ' ' and (board[0][1] == board[1][1] and board[1][1] == board[2][1]):
        result = print(f'{board[0][1]} wygral!')
        return (result)

    if board[0][2] != ' ' and (board[0][2] == board[1][2] and board[1][2] == board[2][2]):
        result = print(f'{board[0][2]} wygral!')
        return (result)


    # krzyzowe (x2):
    if board[0][0] != ' ' and (board[0][0] == board[1][1] and board[1][1] == board[2][2]):
        result = print(f'{board[0][0]} wygral!')
        return (result)

    if board[2][0] != ' ' and (board[2][0] == board[1][1] and board[1][1] == board[0][2]):
        result = print(f'{board[2][0]} wygral!')
        return (result)

    else:
        result = print('Nikt nie wygral.')

    return(result)

tictactoe_check(board_1)
tictactoe_check(board_2)
tictactoe_check(board_3)
tictactoe_check(board_4)
tictactoe_check(board_5)
