# Einfacher Taschenrechner - Dein erstes Python Programm!
# Mini-Projekt aus Stunde 1 des Python & Pygame Kurses

# Erste Eingabe
zahl1 = float(input("Gib die erste Zahl ein: "))

# Operation auswählen
print("\nWähle eine Operation:")
print("+ für Addition")
print("- für Subtraktion")
print("* für Multiplikation")
print("/ für Division")

operation = input("\nDeine Wahl (+, -, *, /): ")

# Zweite Eingabe
zahl2 = float(input("Gib die zweite Zahl ein: "))

# Berechnung durchführen
if operation == "+":
    ergebnis = zahl1 + zahl2
    print(f"\n{zahl1} + {zahl2} = {ergebnis}")

elif operation == "-":
    ergebnis = zahl1 - zahl2
    print(f"\n{zahl1} - {zahl2} = {ergebnis}")

elif operation == "*":
    ergebnis = zahl1 * zahl2
    print(f"\n{zahl1} × {zahl2} = {ergebnis}")

elif operation == "/":
    if zahl2 != 0:
        ergebnis = zahl1 / zahl2
        print(f"\n{zahl1} ÷ {zahl2} = {ergebnis}")
    else:
        print("\nFehler: Division durch Null ist nicht möglich!")

else:
    print("\nUngültige Operation! Bitte verwende +, -, * oder /")
