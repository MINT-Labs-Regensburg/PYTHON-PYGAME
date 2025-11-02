import pygame

# pygame initialisieren
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
pygame.display.set_caption("Kollisionserkennung 💥")

# Rechteck 1 (Spieler - steuerbar)
player_size = 50
player_x = 100
player_y = 100
player_speed = 5

# Rechteck 2 (Ziel - fest)
target_size = 80
target_x = 400
target_y = 300

# Kollisions-Zähler
collision_count = 0
font = pygame.font.Font(None, 36)
clock = pygame.time.Clock()


# Kollisionserkennung Funktion
def check_collision(x1, y1, size1, x2, y2, size2):
    """Prüft ob sich zwei Rechtecke überschneiden"""
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
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < SCREEN_WIDTH - player_size:
        player_x += player_speed
    if keys[pygame.K_UP] and player_y > 0:
        player_y -= player_speed
    if keys[pygame.K_DOWN] and player_y < SCREEN_HEIGHT - player_size:
        player_y += player_speed

    # Kollision prüfen
    was_collision = collision_detected
    collision_detected = check_collision(
        player_x, player_y, player_size, target_x, target_y, target_size
    )

    # Kollisions-Zähler erhöhen (nur bei neuer Kollision)
    if collision_detected and not was_collision:
        collision_count += 1

    # Zeichnen
    screen.fill(WHITE)

    # Spieler-Rechteck (ändert Farbe bei Kollision)
    player_color = GREEN if collision_detected else BLUE
    pygame.draw.rect(
        screen, player_color, (player_x, player_y, player_size, player_size)
    )

    # Ziel-Rechteck
    pygame.draw.rect(screen, RED, (target_x, target_y, target_size, target_size))

    # Kollisions-Zähler anzeigen
    count_text = font.render(f"Kollisionen: {collision_count}", True, BLACK)
    screen.blit(count_text, (10, 10))

    # Anweisungen
    instruction_text = font.render("Pfeiltasten zum Bewegen", True, BLACK)
    screen.blit(instruction_text, (10, 50))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
