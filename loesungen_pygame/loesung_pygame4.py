# Lösung aufgabe_pygame4: Kollisionserkennung mit bewegtem Ziel

import random
import pygame

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

# Spieler (blau, steuerbar)
player_size = 50
player_x = SCREEN_WIDTH // 2 - player_size // 2
player_y = SCREEN_HEIGHT // 2 - player_size // 2
PLAYER_SPEED = 5

# Ziel-Rechteck (rot, bewegt sich zufällig)
target_size = 40
target_x = random.randint(0, SCREEN_WIDTH - target_size)
target_y = random.randint(0, SCREEN_HEIGHT - target_size)
target_dx = random.choice([-3, -2, 2, 3])
target_dy = random.choice([-3, -2, 2, 3])

# Spiel-Variablen
score = 0
clock = pygame.time.Clock()

font = pygame.font.Font(None, 36)


def kollision(player_rect, target_rect):
    """Prüft ob Spieler und Ziel sich berühren. Gibt True zurück bei Kollision."""

    # Ränder des Spielers berechnen
    spieler_links = player_rect.x
    spieler_rechts = player_rect.x + player_rect.width
    spieler_oben = player_rect.y
    spieler_unten = player_rect.y + player_rect.height

    # Ränder des Ziels berechnen
    ziel_links = target_rect.x
    ziel_rechts = target_rect.x + target_rect.width
    ziel_oben = target_rect.y
    ziel_unten = target_rect.y + target_rect.height

    # Kollision liegt vor, wenn sich die Rechtecke auf beiden Achsen überschneiden
    # X-Achse: Spieler ist nicht komplett links oder rechts vom Ziel
    beruehrt_x = spieler_links < ziel_rechts and spieler_rechts > ziel_links

    # Y-Achse: Spieler ist nicht komplett über oder unter dem Ziel
    beruehrt_y = spieler_oben < ziel_unten and spieler_unten > ziel_oben

    # Nur wenn beide Achsen sich überschneiden, gibt es eine Kollision
    return beruehrt_x and beruehrt_y


# Game Loop
running = True
while running:
    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Spieler steuern (Pfeiltasten + WASD)
    keys = pygame.key.get_pressed()
    if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and player_x > 0:
        player_x -= PLAYER_SPEED
    if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and player_x < SCREEN_WIDTH - player_size:
        player_x += PLAYER_SPEED
    if (keys[pygame.K_UP] or keys[pygame.K_w]) and player_y > 0:
        player_y -= PLAYER_SPEED
    if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and player_y < SCREEN_HEIGHT - player_size:
        player_y += PLAYER_SPEED

    # Ziel-Rechteck bewegen
    target_x += target_dx
    target_y += target_dy

    # An Rändern abprallen
    if target_x <= 0 or target_x >= SCREEN_WIDTH - target_size:
        target_dx = -target_dx
        target_x = max(0, min(target_x, SCREEN_WIDTH - target_size))
    if target_y <= 0 or target_y >= SCREEN_HEIGHT - target_size:
        target_dy = -target_dy
        target_y = max(0, min(target_y, SCREEN_HEIGHT - target_size))

    # Kollision prüfen
    player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
    target_rect = pygame.Rect(target_x, target_y, target_size, target_size)

    if kollision(player_rect, target_rect):
        score += 1
        # Ziel an neue zufällige Position setzen und Richtung ändern
        target_x = random.randint(0, SCREEN_WIDTH - target_size)
        target_y = random.randint(0, SCREEN_HEIGHT - target_size)
        target_dx = random.choice([-4, -3, -2, 2, 3, 4])
        target_dy = random.choice([-4, -3, -2, 2, 3, 4])

    # Zeichnen
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, player_rect)
    pygame.draw.rect(screen, RED, target_rect)

    # Score anzeigen
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    info_text = font.render("Pfeiltasten / WASD zum Steuern", True, BLACK)
    screen.blit(info_text, (SCREEN_WIDTH // 2 - info_text.get_width() // 2, SCREEN_HEIGHT - 35))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
