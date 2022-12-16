"""
Niech x oznacza liczbę uzyskanych punktów. Standardowa skala ocen jest następująca:
* x >= 90 -- 5.0
* 90 > x >= 80 -- 4.5
* 80 > x >= 70 -- 4.0
* 70 > x >= 60 -- 3.5
* 60 > x >= 50 -- 3.0
* x < 50 -- 2.0

Zmienna `points` zawiera liczbę uzyskanych punktów przez studenta.
Napisz instrukcję warunką, która wyświetli ocenę studenta w zależności od liczby punktów.
"""

points = 85

grades = {
    range(90,101): '5',
    range(80,90): '4.5',
    range(70,80): '3.5',
    range(60,70): '3.5',
    range(50,60): '3.0',
    range(0,60): '2.0'
    }

for key, value in grades.items():
    if points in key:
        print(f'Ocena: {value}.')