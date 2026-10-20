# Lösung Aufgabe Python 4: Funktionen

# 1. Begrüßungsfunktion definieren
def begruesse(name):
    print(f"Hallo, {name}!")

# 2. Funktion zum Addieren definieren, Due FUnktion gibt das ergebnis zurück
def addiere(a, b):
    summe = a+b
    return summe

# 3. Funktion zum Prüfen gerader Zahlen definieren
def ist_gerade(zahl):
    ergebnis = zahl % 2 == 0
    return ergebnis

# 4. Funktionen mit verschiedenen Werten aufrufen und Rückgabewerte ausgeben
begruesse("Nicole")
begruesse("Max")

summe = addiere(3, 5)
print(f"3 + 5 = {summe}")

summe = addiere(10, 27)
print(f"10 + 27 = {summe}")

print(f"Ist 4 gerade? {ist_gerade(4)}")
print(f"Ist 7 gerade? {ist_gerade(7)}")
