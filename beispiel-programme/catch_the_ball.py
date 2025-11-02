import pygame
import random

# Pygame initialisieren
pygame.init()

# Konstanten
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Screen erstellen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Catch the Ball! 🎯")

# Spieler
player_size = 50
player_x = SCREEN_WIDTH // 2
player_y = SCREEN_HEIGHT - player_size - 10
player_speed = 5

# Ball
ball_size = 30
ball_x = random.randint(0, SCREEN_WIDTH - ball_size)
ball_y = 0
ball_speed = 3

# Spiel-Variablen
score = 0
font = pygame.font.Font(None, 36)
clock = pygame.time.Clock()

# Game Loop
running = True
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

    # Ball bewegen
    ball_y += ball_speed

    # Ball gefangen?
    if (
        player_x < ball_x + ball_size
        and player_x + player_size > ball_x
        and player_y < ball_y + ball_size
        and player_y + player_size > ball_y
    ):
        score += 1

        ball_x = random.randint(0, SCREEN_WIDTH - ball_size)
        ball_y = 0

    # Ball am Boden?
    if ball_y > SCREEN_HEIGHT:
        ball_x = random.randint(0, SCREEN_WIDTH - ball_size)
        ball_y = 0

    # Zeichnen
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, (player_x, player_y, player_size, player_size))
    pygame.draw.circle(
        screen, RED, (ball_x + ball_size // 2, ball_y + ball_size // 2), ball_size // 2
    )

    # Score anzeigen
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
