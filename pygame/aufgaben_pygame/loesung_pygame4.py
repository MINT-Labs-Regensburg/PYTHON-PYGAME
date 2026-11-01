# Lösung aufgabe_pygame4: Kollisionserkennung mit bewegtem Ziel

import random

import pygame

# Pygame initialisieren
pygame.init()

# Konstanten
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)

# Screen erstellen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Kollision - Fang das Rechteck!")

# Spieler vorbereiten
player_size = 50
player_x = SCREEN_WIDTH // 2 - player_size // 2
player_y = SCREEN_HEIGHT // 2 - player_size // 2
PLAYER_SPEED = 5

# Bewegliches Ziel vorbereiten
target_size = 40
target_x = random.randint(0, SCREEN_WIDTH - target_size)
target_y = random.randint(0, SCREEN_HEIGHT - target_size)
target_dx = random.choice([-3, -2, 2, 3])
target_dy = random.choice([-3, -2, 2, 3])

# Spielstand und Zeitsteuerung vorbereiten
score = 0
clock = pygame.time.Clock()

font = pygame.font.Font(None, 36)


def kollision(player_rect, target_rect):
    """Gibt True zurück, wenn Spieler und Ziel sich überschneiden."""

    # Ränder beider Rechtecke berechnen.
    spieler_links = player_rect.x
    spieler_rechts = player_rect.x + player_rect.width
    spieler_oben = player_rect.y
    spieler_unten = player_rect.y + player_rect.height

    ziel_links = target_rect.x
    ziel_rechts = target_rect.x + target_rect.width
    ziel_oben = target_rect.y
    ziel_unten = target_rect.y + target_rect.height

    # Auf beiden Achsen muss eine Überlappung vorliegen.
    beruehrt_x = spieler_links < ziel_rechts and spieler_rechts > ziel_links

    beruehrt_y = spieler_oben < ziel_unten and spieler_unten > ziel_oben

    return beruehrt_x and beruehrt_y


# Hauptschleife
running = True
while running:
    # Ereignisse verarbeiten
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Spieler mit Pfeiltasten oder WASD steuern
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        if player_x >= PLAYER_SPEED:
            player_x -= PLAYER_SPEED
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        if player_x + PLAYER_SPEED <= SCREEN_WIDTH - player_size:
            player_x += PLAYER_SPEED
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        if player_y >= PLAYER_SPEED:
            player_y -= PLAYER_SPEED
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        if player_y + PLAYER_SPEED <= SCREEN_HEIGHT - player_size:
            player_y += PLAYER_SPEED

    # Ziel bewegen
    target_x += target_dx
    target_y += target_dy

    # An den Bildschirmrändern abprallen lassen und im Fenster halten
    if target_x <= 0 or target_x >= SCREEN_WIDTH - target_size:
        target_dx = -target_dx
        target_x = max(0, min(target_x, SCREEN_WIDTH - target_size))
    if target_y <= 0 or target_y >= SCREEN_HEIGHT - target_size:
        target_dy = -target_dy
        target_y = max(0, min(target_y, SCREEN_HEIGHT - target_size))

    # Kollision erkennen
    player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
    target_rect = pygame.Rect(target_x, target_y, target_size, target_size)

    if kollision(player_rect, target_rect):
        score += 1
        # Ziel neu platzieren und seine Geschwindigkeit ändern
        target_x = random.randint(0, SCREEN_WIDTH - target_size)
        target_y = random.randint(0, SCREEN_HEIGHT - target_size)
        target_dx = random.choice([-4, -3, -2, 2, 3, 4])
        target_dy = random.choice([-4, -3, -2, 2, 3, 4])

    # Szene zeichnen
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, player_rect)
    pygame.draw.rect(screen, RED, target_rect)

    # Punktestand anzeigen
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    # Steuerungshinweis anzeigen
    info_text = font.render("Pfeiltasten / WASD zum Steuern", True, BLACK)
    screen.blit(info_text, (SCREEN_WIDTH // 2 - info_text.get_width() // 2, SCREEN_HEIGHT - 35))

    # Anzeige aktualisieren und Bildrate begrenzen
    pygame.display.flip()
    clock.tick(60)

# Pygame beenden
pygame.quit()
