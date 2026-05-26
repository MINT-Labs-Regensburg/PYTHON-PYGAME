# Lösung aufgabe_pygame1: Tastatureingaben

import pygame


pygame.init()

# Konstanten
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
# Screen erstellen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tastatureingaben")

# Rechteck
rect_size = 50
rect_x = SCREEN_WIDTH // 2 - rect_size // 2
rect_y = SCREEN_HEIGHT // 2 - rect_size // 2
RECT_SPEED = 5

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

    # Pfeiltasten
    if keys[pygame.K_LEFT] and rect_x > 0:
        rect_x = rect_x - RECT_SPEED
    if keys[pygame.K_RIGHT] and rect_x < SCREEN_WIDTH - rect_size:
        rect_x = rect_x + RECT_SPEED
    if keys[pygame.K_UP] and rect_y > 0:
        rect_y = rect_y - RECT_SPEED
    if keys[pygame.K_DOWN] and rect_y < SCREEN_HEIGHT - rect_size:
        rect_y = rect_y + RECT_SPEED

    # Alternativ WASD-Steuerung
    if keys[pygame.K_a] and rect_x > 0:
        rect_x = rect_x - RECT_SPEED
    if keys[pygame.K_d] and rect_x < SCREEN_WIDTH - rect_size:
        rect_x = rect_x + RECT_SPEED
    if keys[pygame.K_w] and rect_y > 0:
        rect_y = rect_y - RECT_SPEED
    if keys[pygame.K_s] and rect_y < SCREEN_HEIGHT - rect_size:
        rect_y = rect_y + RECT_SPEED

    # Zeichnen
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, (rect_x, rect_y, rect_size, rect_size))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
