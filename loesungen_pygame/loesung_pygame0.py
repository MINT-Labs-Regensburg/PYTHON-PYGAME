# Lösung aufgabe_pygame0: Dein erstes pygame-Fenster

import pygame


# Pygame initialisieren
pygame.init()

# Fenster erstellen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Mein erstes pygame-Fenster")

# Hauptschleife
running = True
while running:
    # Ereignisse verarbeiten
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Szene zeichnen
    screen.fill((255, 0, 0))

    # Anzeige aktualisieren
    pygame.display.flip()

# Pygame beenden
pygame.quit()