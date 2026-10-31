# Lösung Aufgabe Python 2: If-Statements

# 1. Temperatur beurteilen
temperatur = int(input("Temperatur eingeben: "))
if temperatur > 20:
    print("Schön warm")
else:
    print("Kalt isses")

# 2. Punktzahl einer Note zuordnen
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

# 3. Prüfen, ob eine Frucht in der Liste steht
lieblingsfruechte = ["Apfel", "Banane", "Erdbeere"]
frucht = input("Gib eine Frucht ein: ")
if frucht in lieblingsfruechte:
    print("Das ist eine meiner Lieblingsfrüchte!")
else:
    print("Diese Frucht steht nicht auf meiner Liste.")
