# Lösung aufgabe_pygame1: Tastatureingaben
import pygame

# Pygame initialisieren
pygame.init()

# Konstanten
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
# Fenster erstellen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tastatureingaben")

# Spielobjekt und Zeitsteuerung vorbereiten
rect_size = 50
rect_x = SCREEN_WIDTH // 2 - rect_size // 2
rect_y = SCREEN_HEIGHT // 2 - rect_size // 2
RECT_SPEED = 5

clock = pygame.time.Clock()

# Hauptschleife
running = True
while running:
    # Ereignisse verarbeiten
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Tastatureingaben verarbeiten
    keys = pygame.key.get_pressed()

    # Bewegung mit den Pfeiltasten
    if keys[pygame.K_LEFT]:
        if rect_x >= RECT_SPEED:
            rect_x = rect_x - RECT_SPEED
    if keys[pygame.K_RIGHT]:
        if rect_x + RECT_SPEED <= SCREEN_WIDTH - rect_size:
            rect_x = rect_x + RECT_SPEED
    if keys[pygame.K_UP]:
        if rect_y >= RECT_SPEED:
            rect_y = rect_y - RECT_SPEED
    if keys[pygame.K_DOWN]:
        if rect_y + RECT_SPEED <= SCREEN_HEIGHT - rect_size:
            rect_y = rect_y + RECT_SPEED

    # Alternative Steuerung mit WASD
    if keys[pygame.K_a]:
        if rect_x >= RECT_SPEED:
            rect_x = rect_x - RECT_SPEED
    if keys[pygame.K_d]:
        if rect_x + RECT_SPEED <= SCREEN_WIDTH - rect_size:
            rect_x = rect_x + RECT_SPEED
    if keys[pygame.K_w]:
        if rect_y >= RECT_SPEED:
            rect_y = rect_y - RECT_SPEED
    if keys[pygame.K_s]:
        if rect_y + RECT_SPEED <= SCREEN_HEIGHT - rect_size:
            rect_y = rect_y + RECT_SPEED

    # Szene zeichnen
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, (rect_x, rect_y, rect_size, rect_size))

    # Anzeige aktualisieren und Bildrate begrenzen
    pygame.display.flip()
    clock.tick(60)

# Pygame beenden
pygame.quit()
