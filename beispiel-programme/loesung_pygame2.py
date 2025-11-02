# Lösung Aufgabe 5: Kollisionserkennung

import pygame

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

# Rechteck 1 (beweglich)
rect1_size = 50
rect1_x = 100
rect1_y = 100
rect1_speed = 5

# Rechteck 2 (fest)
rect2_size = 80
rect2_x = 400
rect2_y = 300

# Kollisions-Zähler
collision_count = 0
font = pygame.font.Font(None, 36)
clock = pygame.time.Clock()


# Kollisionserkennung
def check_collision(x1, y1, size1, x2, y2, size2):
    return x1 < x2 + size2 and x1 + size1 > x2 and y1 < y2 + size2 and y1 + size1 > y2


# Game Loop
running = True
collision_detected = False

while running:
    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Tastatureingaben
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and rect1_x > 0:
        rect1_x -= rect1_speed
    if keys[pygame.K_RIGHT] and rect1_x < SCREEN_WIDTH - rect1_size:
        rect1_x += rect1_speed
    if keys[pygame.K_UP] and rect1_y > 0:
        rect1_y -= rect1_speed
    if keys[pygame.K_DOWN] and rect1_y < SCREEN_HEIGHT - rect1_size:
        rect1_y += rect1_speed

    # Kollision prüfen
    was_collision = collision_detected
    collision_detected = check_collision(
        rect1_x, rect1_y, rect1_size, rect2_x, rect2_y, rect2_size
    )

    # Kollisions-Zähler erhöhen
    if collision_detected and not was_collision:
        collision_count += 1

    # Zeichnen
    screen.fill(WHITE)

    # Rechtecke zeichnen (Farbe ändert sich bei Kollision)
    rect1_color = GREEN if collision_detected else BLUE
    pygame.draw.rect(screen, rect1_color, (rect1_x, rect1_y, rect1_size, rect1_size))
    pygame.draw.rect(screen, RED, (rect2_x, rect2_y, rect2_size, rect2_size))

    # Kollisions-Zähler anzeigen
    count_text = font.render(f"Kollisionen: {collision_count}", True, BLACK)
    screen.blit(count_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
