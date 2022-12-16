"""
Lista iris_setosa zawiera informacje o 4 egzemplarzach kosacieca szczecinkowego.
Pierwszy indeks to długość kwiata.
Drugi indeks to szerokość kwiata.
Trzeci indeks to długość liścia.
Czwarty indeks to szerokość liścia.

* Oblicz średnią szerokość kwiata.
* Dodaj do listy dane o nowym egzemplarzu: (5.4, 3.9, 1.7, 0.4)
"""

iris_setosa  = [
    [5.1, 3.5, 1.4, 0.2],
    [4.9, 3, 1.4, 0.2],
    [4.7, 3.2, 1.3, 0.2],
]

#A
srednia = 0
for item in iris_setosa:
    srednia += item[0]*item[1]
print(srednia/len(iris_setosa))

#B
iris_setosa.append([5.4, 3.9, 1.7, 0.4])
print(iris_setosa)

srednia = 0
for item in iris_setosa:
    srednia += item[0]*item[1]
print(srednia/len(iris_setosa))
