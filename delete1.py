import pygame

# Dein erstes Pygame-Fenster!
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
