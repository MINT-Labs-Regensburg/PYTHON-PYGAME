# Lösung aufgabe_pygame2: Kollisionserkennung

import pygame

# Pygame initialisieren
pygame.init()

# Konstanten
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Screen erstellen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Kollisionserkennung")

# Spielobjekte vorbereiten
# Bewegliches Rechteck
rect1_size = 50
rect1_x = 100
rect1_y = 100
rect1_speed = 5

# Festes Rechteck
rect2_size = 80
rect2_x = 400
rect2_y = 300

# Spielstand und Zeitsteuerung vorbereiten
collision_count = 0
font = pygame.font.Font(None, 36)
clock = pygame.time.Clock()


# Kollisionserkennung
def check_collision(x1, y1, size1, x2, y2, size2):
    # Eine Kollision liegt vor, wenn sich beide Achsen überschneiden.
    beruehrt_horizontal = x1 < x2 + size2 and x1 + size1 > x2
    beruehrt_vertikal = y1 < y2 + size2 and y1 + size1 > y2

    return beruehrt_horizontal and beruehrt_vertikal


# Hauptschleife
running = True
collision_detected = False

while running:
    # Ereignisse verarbeiten
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Tastatureingaben verarbeiten
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and rect1_x > 0:
        rect1_x -= rect1_speed
    if keys[pygame.K_RIGHT] and rect1_x < SCREEN_WIDTH - rect1_size:
        rect1_x += rect1_speed
    if keys[pygame.K_UP] and rect1_y > 0:
        rect1_y -= rect1_speed
    if keys[pygame.K_DOWN] and rect1_y < SCREEN_HEIGHT - rect1_size:
        rect1_y += rect1_speed

    # Kollision erkennen
    was_collision = collision_detected
    collision_detected = check_collision(
        rect1_x, rect1_y, rect1_size, rect2_x, rect2_y, rect2_size
    )

    # Pro Berührung nur einmal zählen.
    if collision_detected and not was_collision:
        collision_count += 1

    # Szene zeichnen
    screen.fill(WHITE)

    # Rechtecke zeichnen; das bewegliche Rechteck wechselt bei Kollision die Farbe.
    rect1_color = GREEN if collision_detected else BLUE
    pygame.draw.rect(screen, rect1_color, (rect1_x, rect1_y, rect1_size, rect1_size))
    pygame.draw.rect(screen, RED, (rect2_x, rect2_y, rect2_size, rect2_size))

    # Kollisionszahl anzeigen
    count_text = font.render(f"Kollisionen: {collision_count}", True, BLACK)
    screen.blit(count_text, (10, 10))

    # Anzeige aktualisieren und Bildrate begrenzen
    pygame.display.flip()
    clock.tick(60)

# Pygame beenden
pygame.quit()
