# Einfaches Ratespiel - Mini-Projekt aus Stunde 2
# Python & Pygame Kurs

import random

# Computer wählt eine Zahl zwischen 1 und 10
geheime_zahl = random.randint(1, 10)

print("Ratespiel: Ich denke an eine Zahl zwischen 1 und 10!")
print("Du hast 3 Versuche!")

# 3 Versuche für den Spieler
for versuch in range(1, 4):
    print(f"\nVersuch {versuch}:")

    # Spieler gibt Tipp ab
    tipp = int(input("Dein Tipp: "))

    # Prüfen ob richtig
    if tipp == geheime_zahl:
        print(f"Richtig! Die Zahl war {geheime_zahl}")
        print("Du hast gewonnen!")
        break
    elif tipp < geheime_zahl:
        print("Zu klein!")
    else:
        print("Zu groß!")

    # Nach dem 3. Versuch
    if versuch == 3:
        print(f"\nLeider verloren! Die Zahl war {geheime_zahl}")

print("Spiel beendet!")
