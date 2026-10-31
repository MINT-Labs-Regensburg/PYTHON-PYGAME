# Lösung Aufgabe Python 3: Schleifen

# 1. Zahlen von 1 bis 10 mit einer for-Schleife ausgeben
print("Zählen von 1 bis 10:")
for i in range(1, 11):
    print(i)

print()

# 2. Alle Früchte aus einer Liste ausgeben
obst = ["Apfel", "Banane", "Birne", "Orange"]
print("Mein Lieblingsobst:")
for frucht in obst:
    print(frucht)

print()

# 3. Countdown mit einer while-Schleife ausgeben
print("Countdown:")
countdown = 10
while countdown > 0:
    print(countdown)
    countdown -= 1
print("START!")

print()

# 4. Kleines Einmaleins für die Zahl 5 ausgeben
print("Das kleine 1x1 für die Zahl 5:")
for i in range(1, 11):
    print(f"{i} * 5 = {i * 5}")

print()

# 5. Gerade Zahlen von 1 bis 20 finden und ausgeben
print("Gerade Zahlen von 1 bis 20:")
for zahl in range(1, 21):
    if zahl % 2 == 0:
        print(zahl)
