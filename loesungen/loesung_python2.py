# Lösung Aufgabe 2: If-Statements

# 1. Temperatur-Check
temperatur = int(input("Temperatur eingeben: "))
if temperatur > 20:
    print("Schön warm")
else:
    print("Kalt isses")

# 2. Notensystem
note = int(input("Gib deine Punktzahl ein: "))
if note >= 90:
    print("Sehr gut!")
elif note >= 80:
    print("Gut!")
elif note >= 70:
    print("Befriedigend")
elif note >= 60:
    print("Ausreichend")
else:
    print("Durchgefallen")
