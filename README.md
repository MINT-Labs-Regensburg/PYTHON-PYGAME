# Python & Pygame Kurs - Gaming Adventure!

Willkommen zu unserem Python & Pygame Kurs!

---

## 💝 Herzlichen Dank

| Ein herzliches Dankeschön an **Dr. Norwin von Malm** und **Stefan Grötsch** – die Preisträger des [Deutschen Zukunftspreises 2024](https://www.deutscher-zukunftspreis.de/de/team-1-2024)<br><br>Mit ihrer Spende und ihrer großzügigen Unterstützung haben Sie die Entwicklung und Durchführung dieses Kurses ermöglicht. | <img src="assets/DZP_Logo_2.svg" alt="DZP Logo" width="120"/> |
|:---|:---:|

---

## Was erwartet dich?

In diesem Kurs wirst du:
- **Python** von Grund auf lernen *(keine Sorge, ist einfacher als du denkst!)*
- Dein **erstes eigenes Spiel** mit **pygame** entwickeln
- **Visual Studio Code** wie ein Profi verwenden

---

## Was brauchst du?

### Software Installation
*haben wir hier bereits für dich installiert. Kannst du zu Hause kostenlos runterladen*

1. **Python 3.x** - Die Programmiersprache unserer Wahl
2. **Visual Studio Code** - Unser cooler Code-Editor
3. **pygame** - Die Gaming-Bibliothek, die alles möglich macht
4. **Cheat-sheets** - Übersicht über die wichtigsten Befehle:
   - [Python Cheatsheet](assets/python-cheat-sheet.pdf)
   - [pygame Cheatsheet deutsch](assets/pygame-cheat-sheet.pdf)
   - [pygame Cheatsheet](assets/rootix_basic-pygame.pdf)

### Hardware
- Einen Computer mit Tastatur un Maus
- *Geht auch auf deinem Computer zu Hause oder einem Raspberry Pi4*

---

## Kursdurchführung

### Teil 1: So startest du Python in Visual Studio Code

**Schritt-für-Schritt Anleitung:**
1. **VS Code öffnen** - Doppelklick auf das Icon
2. **Neue Datei** - `Strg + N` drücken
3. **Als Python speichern** - `Strg + S` → Name eingeben mit `.py` am Ende *(z.B. `mein_programm.py`)*
4. **Code schreiben** - Einfach lostippen!
5. **Programm starten** - `F5` drücken oder rechte Maustaste → "Run Python File"
6. **Ausgabe sehen** - Unten im Terminal erscheint das Ergebnis

#### Dein erstes Python-Programm:
```python
print("Hello World!")
```

---

### Teil 2: "Python - Listen, Schleifen, Funktionen & Co."

**Was lernst du:**
- **Listen** - Wie man Daten organisiert
- **If-Else Statements** - Deinem Programm Entscheidungen beibringen
- **Schleifen** - Lass den Computer für dich arbeiten!
- **Funktionen** - Code wiederverwenden und Parameter übergeben


**Aufgabe 1: Variablen**
1. Erstelle Variablen für `name`, `alter` und `groesse`
2. Gib sie mit `print()` aus. **Beispiel:** `Ich heisse Nicole bin 12 Jahre alt und 1.57 Meter gross`
3. Verändere das `alter` um +1 
4. Berechne `summe` von zwei Zahlen
5. Frage den Nutzer nach seiner Lieblingsfarbe with `input()`

**Aufgabe 2: If-Statements**

1. **Temperatur-Check:** Schreibe ein `if-else` für Temperatur. Ist die mit `input()` eingegebene Temperatur > 20, schreibe "schön warm" sonst schreibe "kalt isses"

2. **Notensystem:** Baue ein Notensystem mit `if-elif-else` *(90+ = Sehr gut, 80+ = Gut, etc.)*


**Aufgabe 3: Schleifen**
1. Zähle von 1 bis 10 mit `for i in range(1, 11)`
2. Gib alle Früchte aus einer Liste aus
3. Mache einen Countdown with `while`.  `10 9 8 7 6 5 4 3 2 1 START`
4. Programmiere das kleine 1x1 für die Zahl 5
5. Finde alle geraden Zahlen von 1-20 with `if zahl % 2 == 0`


**Aufgabe 4: Funktionen**
1. Schreibe eine Funktion `begruesse(name)`, die `"Hallo, <name>!"` ausgibt
2. Schreibe eine Funktion `addiere(a, b)`, die die Summe zweier Zahlen zurückgibt und ausgibt
3. Schreibe eine Funktion `ist_gerade(zahl)`, die `True` oder `False` zurückgibt
4. Rufe jede Funktion mit verschiedenen Werten auf

**Zusatzaufgabe:** Programmiere einen simplen Taschenrechner. Zwei Zahlen und Grundrechenarten  [Beispiel-Code hier](loesungen/taschenrechner.py)


---

# 🎮 Jetzt gehts los mit pygame

### Teil 3: "pygame Installation & Erste Grafiken"

**Was lernst du:**
- **pygame Installation** -  `pip install pygame-ce`
- **Fenster erstellen** - Dein erstes Game-Fenster
- **Farben und Formen** - Rechtecke, Kreise und was das Herz begehrt
- **Mini-Projekt:** Ein buntes, sich bewegendes Rechteck

### Unser pygame braucht mindestens diese Elemente:

- **`import pygame`** - Lade die pygame-Bibliothek
- **`pygame.init()`** - Initialisiere alle pygame-Module
- **`screen = pygame.display.set_mode((800, 600))`** - Erstelle ein Fenster mit 800x600 Pixeln
- **`pygame.display.set_caption("Titel")`** - Setze den Fenstertitel
- **`running = True`** - Variable für die Hauptschleife
- **`while running:`** - Hauptschleife (Game Loop) - läuft bis das Spiel beendet wird
- **`for event in pygame.event.get():`** - Verarbeite alle Events (Maus, Tastatur, etc.)
- **`if event.type == pygame.QUIT:`** - Prüfe ob das Fenster geschlossen wurde
- **`screen.fill((255, 0, 0))`** - Fülle den Bildschirm mit einer Farbe (RGB-Werte)
- **`pygame.display.flip()`** - Aktualisiere das Display
- **`pygame.quit()`** - Beende pygame ordnungsgemäß

### Minimales pygame Programm:
```python
import pygame

# Dein erstes pygame-Fenster!
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Mein erstes Spiel! 🎮")

# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((255, 0, 0))  # Roter Hintergrund
    pygame.display.flip()

pygame.quit()
```

---

### Teil 4: "Game Development - Bewegung und Interaktion"

**Was lernst du:**
- **Tastatureingaben** - Steuerung deiner Spielfigur
- **Kollisionserkennung** - Wenn Objekte aufeinandertreffen
- **Mini-Projekt:** Ein einfaches "Catch the Ball" Spiel

**Aufgabe 4: Tastatureingaben**
1. Erstelle ein Rechteck, das sich mit den Pfeiltasten bewegt
2. Füge WASD-Steuerung hinzu (W=hoch, A=links, S=runter, D=rechts)
3. Lass das Rechteck schneller werden, wenn Shift gedrückt wird

**Aufgabe 5: Kollisionserkennung**
1. Erstelle zwei Rechtecke und erkenne, wenn sie sich berühren
2. Ändere die Farbe bei einer Kollision
3. Zähle die Anzahl der Kollisionen und zeige sie an

- [Beispiel-Code Kollisionserkennung](loesungen/loesung_pygame2.py)

**Zusatzaufgabe:** Programmiere ein "Catch the Ball" Spiel mit folgenden Anforderungen:
1. Programmiere ein "Catch the Ball" Spiel
2. Füge einen Score-Counter hinzu
3. Baue einen Timer ein (30 Sekunden Spielzeit)

- [Beispiel-Code Catch the Ball](loesungen/loesung_pygame3.py)

---


## Mögliche Spielideen

- **Pong** - Der Klassiker für Einsteiger
- **Snake** - Das legendäre Schlangen-Spiel
- **Space Invaders** - Aliens abschießen im Weltraum
- **Plattformspiel** - Springe durch verschiedene Level
- **Dein eigenes Spiel** - Sei kreativ und überrasche uns!

---




*Happy coding 🚀*

## Mehr Projekte und Anleitungen findest du [hier](https://wiki.mint-labs.de/)
