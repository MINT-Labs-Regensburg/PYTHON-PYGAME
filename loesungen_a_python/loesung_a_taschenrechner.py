# Einfacher Taschenrechner - Dein erstes Python Programm!
# Mini-Projekt aus Stunde 1 des Python & Pygame Kurses

# Erste Zahl eingeben
erste_zahl = float(input("Gib die erste Zahl ein: "))

# Operation auswählen
print("\nWähle eine Operation:")
print("+ für Addition")
print("- für Subtraktion")
print("* für Multiplikation")
print("/ für Division")

operation = input("\nDeine Wahl (+, -, *, /): ")

# Zweite Zahl eingeben
zweite_zahl = float(input("Gib die zweite Zahl ein: "))

# Berechnung durchführen
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
