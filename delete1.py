# Lösung Aufgabe 4: Funktionen

# 1. Funktion begruesse(name) – gibt "Hallo, <name>!" aus
def begruesse(name):
    print(f"Hallo, {name}!")

# 2. Funktion addiere(a, b) – gibt die Summe zurück und gibt sie aus
def addiere(a, b):
    summe = a + b
    print(f"{a} + {b} = {summe}")
    return summe

# 3. Funktion ist_gerade(zahl) – gibt True oder False zurück
def ist_gerade(zahl):
    return zahl % 2 == 0

# 4. Jede Funktion mit verschiedenen Werten aufrufen
begruesse("Nicole")
begruesse("Max")

addiere(3, 5)
addiere(10, 27)

print(ist_gerade(4))   # True
print(ist_gerade(7))   # False