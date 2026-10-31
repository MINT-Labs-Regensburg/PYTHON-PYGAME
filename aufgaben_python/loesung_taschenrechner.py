# Lösung: Einfacher Taschenrechner
# Mini-Projekt aus Stunde 1 des Python & Pygame Kurses

# 1. Erste Zahl abfragen
erste_zahl = float(input("Gib die erste Zahl ein: "))

# 2. Rechenoperation auswählen
print("\nWähle eine Operation:")
print("+ für Addition")
print("- für Subtraktion")
print("* für Multiplikation")
print("/ für Division")

operation = input("\nDeine Wahl (+, -, *, /): ")

# 3. Zweite Zahl abfragen
zweite_zahl = float(input("Gib die zweite Zahl ein: "))

# 4. Berechnung durchführen und Ergebnis ausgeben
if operation == "+":
    ergebnis = erste_zahl + zweite_zahl
    print(f"\n{erste_zahl} + {zweite_zahl} = {ergebnis}")

elif operation == "-":
    ergebnis = erste_zahl - zweite_zahl
    print(f"\n{erste_zahl} - {zweite_zahl} = {ergebnis}")

elif operation == "*":
    ergebnis = erste_zahl * zweite_zahl
    print(f"\n{erste_zahl} × {zweite_zahl} = {ergebnis}")

elif operation == "/":
    if zweite_zahl != 0:
        ergebnis = erste_zahl / zweite_zahl
        print(f"\n{erste_zahl} / {zweite_zahl} = {ergebnis}")
    else:
        print("\nFehler: Division durch Null ist nicht möglich!")

else:
    print("\nUngültige Operation! Bitte verwende +, -, * oder /")
