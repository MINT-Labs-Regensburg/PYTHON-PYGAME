# Lösung Aufgabe 3: Schleifen

# 1. Zähle von 1 bis 10 mit for i in range(1, 11)
print("Zählen von 1 bis 10:")
for i in range(1, 11):
    print(i)

print()

# 2. Gib alle Früchte aus einer Liste aus
obst = ["Apfel", "Banane", "Birne", "Orange"]
print("Mein Lieblingsobst:")
for frucht in obst:
    print(f"- {frucht}")

print()

# 3. Mache einen Countdown mit while
print("Countdown:")
countdown = 10
while countdown > 0:
    print(countdown)
    countdown -= 1
print("START!")

print()

# 4. Programmiere das kleine 1x1 für die Zahl 5
print("Das kleine 1x1 für die Zahl 5:")
for i in range(1, 11):
    print(f"{i} * 5 = {i * 5}")

print()

# 5. Finde alle geraden Zahlen von 1-20
print("Gerade Zahlen von 1 bis 20:")
for zahl in range(1, 21):
    if zahl % 2 == 0:
        print(zahl)
