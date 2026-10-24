# Lösung aufgabe_pygame3: Game Mechanics

import os
import random

import pygame

# Pygame initialisieren
pygame.init()

# Konstanten
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GAME_TIME_SECONDS = 30
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Screen erstellen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Catch the Ball - Game Mechanics")

# Spieler vorbereiten
player_size = 70
player_x = SCREEN_WIDTH // 2 - player_size // 2
player_y = SCREEN_HEIGHT - player_size - 20
player_speed = 7

# Ball vorbereiten
ball_size = 30
ball_x = random.randint(0, SCREEN_WIDTH - ball_size)
ball_y = 0
ball_speed = 4

# Spielstand und Zeitmessung vorbereiten
score = 0
clock = pygame.time.Clock()
start_time = pygame.time.get_ticks()

# Schrift laden, falls das Font-Modul verfügbar ist
font = None
if hasattr(pygame, "font"):
    try:
        font = pygame.font.Font(None, 36)
    except (NotImplementedError, AttributeError):
        font = None

# Sounds laden, falls Mixer und Dateien verfügbar sind
hit_sound = None
miss_sound = None
try:
    pygame.mixer.init()
    hit_sound_path = os.path.join(os.path.dirname(__file__), "..", "assets", "hit.wav")
    miss_sound_path = os.path.join(os.path.dirname(__file__), "..", "assets", "miss.wav")
    if os.path.exists(hit_sound_path):
        hit_sound = pygame.mixer.Sound(hit_sound_path)
    if os.path.exists(miss_sound_path):
        miss_sound = pygame.mixer.Sound(miss_sound_path)
except pygame.error:
    hit_sound = None
    miss_sound = None

# Hauptschleife
running = True
while running:
    # Ereignisse verarbeiten
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Verbleibende Spielzeit berechnen
    elapsed_ms = pygame.time.get_ticks() - start_time
    time_left = max(0, GAME_TIME_SECONDS - elapsed_ms // 1000)
    if time_left == 0:
        running = False

    # Tastatureingaben verarbeiten
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        if player_x >= player_speed:
            player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        if player_x + player_speed <= SCREEN_WIDTH - player_size:
            player_x += player_speed

    # Ball bewegen
    ball_y += ball_speed

    # Treffer erkennen und Spielstand erhöhen
    if (
        player_x < ball_x + ball_size
        and player_x + player_size > ball_x
        and player_y < ball_y + ball_size
        and player_y + player_size > ball_y
    ):
        score += 1
        if hit_sound is not None:
            hit_sound.play()

        ball_x = random.randint(0, SCREEN_WIDTH - ball_size)
        ball_y = 0

    # Verpassten Ball zurücksetzen
    if ball_y > SCREEN_HEIGHT:
        if miss_sound is not None:
            miss_sound.play()
        ball_x = random.randint(0, SCREEN_WIDTH - ball_size)
        ball_y = 0

    # Szene zeichnen
    screen.fill(WHITE)
    # Spieler und Ball zeichnen
    pygame.draw.rect(screen, BLUE, (player_x, player_y, player_size, player_size))
    pygame.draw.circle(
        screen, RED, (ball_x + ball_size // 2, ball_y + ball_size // 2), ball_size // 2
    )

    # Spielstand und Zeit anzeigen, falls eine Schrift verfügbar ist
    if font is not None:
        score_text = font.render(f"Score: {score}", True, BLACK)
        timer_text = font.render(f"Zeit: {time_left}s", True, BLACK)
        screen.blit(score_text, (10, 10))
        screen.blit(timer_text, (10, 45))

    # Anzeige aktualisieren und Bildrate begrenzen
    pygame.display.flip()
    clock.tick(60)

# Endbild kurz anzeigen
if font is not None:
    screen.fill(WHITE)
    end_text = font.render(f"Zeit vorbei! Endscore: {score}", True, BLACK)
    screen.blit(end_text, (SCREEN_WIDTH // 2 - 170, SCREEN_HEIGHT // 2 - 20))
    pygame.display.flip()
    pygame.time.wait(2000)

# Pygame beenden
pygame.quit()
