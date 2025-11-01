# name = "Nicole"
# alter = 12
# groesse = 1.57
# alter += 1

# print("Ich heisse", name, "bin", alter, "Jahre alt und", groesse, "Meter gross")

# lieblingsfarbe = input("Was ist deine Lieblingsfarbe? ")
# print(f"Deine Lieblingsfarbe ist {lieblingsfarbe}")


# temperatur = int(input("Temperatur eingeben: "))
# if temperatur > 20:
#     print("Ganz schön warm")
# else:
#     print("Kalt isses")


for i in range(1, 11):
    print(i)


obst = ["Apfel", "Banane", "Birne"]

# Methode 1: Ganze Liste
print(obst)

# Methode 2: Jedes Element einzeln mit for-Schleife
for frucht in obst:
    print(frucht)

# # Methode 3: Mit schöner Formatierung
# print("Mein Lieblingsobst:")
# for frucht in obst:
#     print(f"- {frucht}")

# # Methode 4: Einzelne Elemente per Index
# print(obst[0])  # Erstes Element (Apfel)
# print(obst[1])  # Zweites Element (Banane)
# print(obst[2])  # Drittes Element (Birne)

# Countdown mit while-Schleife
countdown = 10
while countdown > 0:
    print(countdown)
    countdown -= 1
print("Start!")

for i in range(1,6):
    print(i, "* 5 =", i*5)

for i in range(1,21):
    if i % 2 == 0:
        print(i)