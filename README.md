# 🎮 Python & Pygame Kurs - Gaming Adventure! 🐍

Willkommen zu unserem Python & Pygame Kurs! 🚀

---

## 💝 Herzlichen Dank

| Ein herzliches Dankeschön an **Dr. Norwin von Malm** und **Stefan Grötsch** – die Preisträger des [Deutschen Zukunftspreises 2024](https://www.deutscher-zukunftspreis.de/de/team-1-2024).<br><br>Mit ihrer Spende und ihrer großzügigen Unterstützung haben Sie die Entwicklung und Durchführung dieses Kurses ermöglicht. 🙏 | <img src="assets/DZP_Logo_2.svg" alt="DZP Logo" width="120"/> |
|:---|:---:|

---

## 🎯 Was erwartet dich?

In diesem Kurs wirst du:
- 🐍 **Python** von Grund auf lernen *(keine Sorge, ist einfacher als du denkst!)*
- 🎮 Dein **erstes eigenes Spiel** mit **Pygame** entwickeln
- 💻 **Visual Studio Code** wie ein Profi verwenden

---

## 🛠️ Was brauchst du?

### 📦 Software Installation
*haben wir hier bereits für dich installiert. Kannst du zu Hause kostenlos runterladen*

1. 🐍 **Python 3.x** - Die Programmiersprache unserer Wahl
2. 💻 **Visual Studio Code** - Unser cooler Code-Editor
3. 🎮 **Pygame** - Die Gaming-Bibliothek, die alles möglich macht
4. 📋 **Cheat-sheets** - Übersicht über die wichtigsten Befehle:
   - [Python Cheatsheet](assets/python-cheat-sheet.pdf) 📄
   - [Pygame Cheatsheet](assets/pygame-cheats-heet.pdf) 📄

### 💻 Hardware
- ✅ Einen Computer *(offensichtlich 😄)*
- ✅ Tastatur und Maus
- ✅ *Geht auch auf deinem Computer zu Hause oder einem Raspberry Pi4*

---

## 📚 Kursprogramm

### 🏁 Teil 1: So startest du Python in Visual Studio Code

**Schritt-für-Schritt Anleitung:**
1. 🖱️ **VS Code öffnen** - Doppelklick auf das Icon
2. 📄 **Neue Datei** - `Strg + N` drücken
3. 💾 **Als Python speichern** - `Strg + S` → Name eingeben mit `.py` am Ende *(z.B. `mein_programm.py`)*
4. ⌨️ **Code schreiben** - Einfach lostippen!
5. ▶️ **Programm starten** - `F5` drücken oder rechte Maustaste → "Run Python File"
6. 📺 **Ausgabe sehen** - Unten im Terminal erscheint das Ergebnis

#### 🌟 Dein erstes Python-Programm:
```python
print("Hello World!")
```

---

### 🕑 Teil 2: "Python Power-Up - Listen, Schleifen & Co."

**Was lernst du:**
- 📝 **Listen und Dictionaries** - Wie man Daten organisiert
- 🤔 **If-Else Statements** - Deinem Programm Entscheidungen beibringen
- 🔄 **Schleifen** - Lass den Computer für dich arbeiten!


#### 📋 Aufgaben für Teil 2:

**🎯 Aufgabe 1: Variablen - Schritt für Schritt**
1. ✏️ Erstelle Variablen für `name`, `alter` und `groesse`
2. 🖨️ Gib sie mit `print()` aus. **Beispiel:** `Ich heisse Nicole bin 12 Jahre alt und 1.57 Meter gross`
3. ➕ Verändere das `alter` um +1 
4. 🧮 Berechne `summe` von zwei Zahlen
5. ❓ Frage den Nutzer nach seiner Lieblingsfarbe mit `input()`

**🎯 Aufgabe 2: If-Statements**
1. 🌡️ Schreibe ein `if` für Temperatur > 20
2. 🔞 Erweitere es zu `if-else` für Alter >= 18
3. 📊 Baue ein Notensystem mit `if-elif-else` *(90+ = Sehr gut, 80+ = Gut, etc.)*


**🎯 Aufgabe 3: Schleifen**
1. 🔢 Zähle von 1 bis 10 mit `for i in range(1, 11)`
2. 🍎 Gib alle Früchte aus einer Liste aus
3. ⏰ Mache einen Countdown mit `while`
4. ✖️ Programmiere das kleine 1x1 für die Zahl 5
5. 🔢 Finde alle geraden Zahlen von 1-20 mit `if zahl % 2 == 0`

**🌟 Zusatzaufgabe:** Einen simplen Taschenrechner programmieren. [Beispiel-Code hier](beispiel-programme/taschenrechner.py)

---

### 🕒 Teil 3: "Pygame Installation & Erste Grafiken"

**Was lernst du:**
- 🎊 **Pygame Installation** - Let's get this party started!
- 🪟 **Fenster erstellen** - Dein erstes Game-Fenster
- 🎨 **Farben und Formen** - Rechtecke, Kreise und was das Herz begehrt
- 🚀 **Mini-Projekt:** Ein buntes, sich bewegendes Rechteck

```python
import pygame

# Dein erstes Pygame-Fenster!
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Mein erstes Spiel! 🎮")
```

---

### 🕓 Teil 4: "Game Development - Bewegung und Interaktion"

**Was lernst du:**
- ⌨️ **Tastatureingaben** - Steuerung deiner Spielfigur
- 💥 **Kollisionserkennung** - Wenn Objekte aufeinandertreffen
- 🔊 **Sounds und Musik** - Akustische Effekte für mehr Atmosphäre
- 🎯 **Mini-Projekt:** Ein einfaches "Catch the Ball" Spiel

---

### 🕔 Teil 5: "Dein eigenes Spiel - Kreativität ist gefragt!"

**Was lernst du:**
- 📋 **Projektplanung** - Was für ein Spiel willst du machen?
- 🎨 **Freie Entwicklungszeit** - Lass deiner Fantasie freien Lauf!
- 🐛 **Debugging** - Fehler finden und beheben *(gehört dazu!)*
- 🏆 **Präsentation** - Zeig uns dein Meisterwerk!

---

## 🎮 Mögliche Spielideen

- 🏓 **Pong** - Der Klassiker für Einsteiger
- 🐍 **Snake** - Das legendäre Schlangen-Spiel
- 👾 **Space Invaders** - Aliens abschießen im Weltraum
- 🦘 **Plattformspiel** - Springe durch verschiedene Level
- 💡 **Dein eigenes Spiel** - Sei kreativ und überrasche uns!

---

## 💡 Hilfreiche Tipps

### 🔧 VS Code Extensions 
- 🐍 **Python Extension** - Für bessere Python-Unterstützung
- ✅ **Pylint** - Hilft dir, sauberen Code zu schreiben
- 📝 **Python Docstring Generator** - Für professionelle Dokumentation

### 🐛 Debugging Tipps
- 😌 **Keine Panik bei Fehlern!** - Fehler sind normal und helfen beim Lernen
- 🖨️ **print()** ist dein Freund - Nutze es zum Debuggen
- 🔍 **Google ist dein bester Kumpel** - Stackoverflow kennt alle Antworten
- 🙋 **Frag einfach!** - Keine Frage ist dumm

### 🎨 Kreativitäts-Booster
- 🖼️ **Kostenlose Grafiken:** [OpenGameArt.org](https://opengameart.org/)
- 🔊 **Gratis Sounds:** [Freesound.org](https://freesound.org/)
- 🌈 **Farbpaletten:** [Coolors.co](https://coolors.co/)

---

## 🚀 Nach dem Kurs

### 🎓 Was kannst du danach?
- ✅ Python-Programme schreiben
- ✅ Einfache Spiele mit Pygame entwickeln
- ✅ Visual Studio Code professionell nutzen
- ✅ Eigene Projekte starten
- ✅ Mit anderen Programmierern sprechen *(du kennst jetzt die Geheimsprache! 🤫)*

### 📚 Weiterführende Ressourcen
- 🐍 **Python.org** - Die offizielle Python-Website
- 📖 **Real Python** - Tutorials für alle Levels
- 🎮 **Pygame Tutorials** - Vertiefe dein Gaming-Wissen
- 🌍 **GitHub** - Teile deine Projekte mit der Welt

---

## 🎉 Fun Facts

- 🎭 **Python** wurde nach "Monty Python's Flying Circus" benannt!
- 🎮 **Pygame** wird für professionelle Spiele verwendet
- 💻 **Visual Studio Code** ist einer der beliebtesten Code-Editoren weltweit
- 🎊 Du wirst nach diesem Kurs offiziell ein **Programmierer** sein! 👨‍💻👩‍💻

---

*Viel Spaß beim Programmieren! 🚀*

