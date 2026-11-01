import pygame
import sys

pygame.init()

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 550
FPS = 60

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
SKY = (30, 30, 60)
GROUND_COLOR = (60, 180, 60)
PLATFORM_COLOR = (120, 80, 40)
PLATFORM_TOP = (80, 200, 80)
PLAYER_COLOR = (60, 140, 240)
PLAYER_EYE = (255, 255, 255)
COIN_COLOR = (240, 200, 0)
SPIKE_COLOR = (200, 50, 50)
GOAL_COLOR = (255, 220, 0)
GRAY = (80, 80, 80)
HUD_COLOR = (220, 220, 220)

GRAVITY = 0.6
JUMP_FORCE = -13
PLAYER_SPEED = 4

font_large = pygame.font.SysFont("monospace", 64, bold=True)
font_med = pygame.font.SysFont("monospace", 32, bold=True)
font_small = pygame.font.SysFont("monospace", 22)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Plattformspiel")
clock = pygame.time.Clock()

# -------------------------------------------------------------------
# Level-Daten: (x, y, width, height)
# Alle Koordinaten in Welt-Koordinaten (Kamera scrollt horizontal)
# -------------------------------------------------------------------
WORLD_WIDTH = 3600

PLATFORMS = [
    # Boden
    pygame.Rect(0, 500, 3600, 60),
    # Plattformen Level 1
    pygame.Rect(200, 400, 120, 18),
    pygame.Rect(380, 320, 100, 18),
    pygame.Rect(520, 240, 130, 18),
    pygame.Rect(700, 310, 110, 18),
    pygame.Rect(860, 400, 140, 18),
    pygame.Rect(1040, 310, 100, 18),
    pygame.Rect(1180, 220, 120, 18),
    pygame.Rect(1360, 300, 110, 18),
    pygame.Rect(1500, 400, 130, 18),
    pygame.Rect(1660, 300, 100, 18),
    pygame.Rect(1800, 210, 120, 18),
    pygame.Rect(1980, 310, 110, 18),
    pygame.Rect(2140, 400, 130, 18),
    pygame.Rect(2300, 300, 100, 18),
    pygame.Rect(2450, 210, 120, 18),
    pygame.Rect(2620, 320, 110, 18),
    pygame.Rect(2780, 230, 130, 18),
    pygame.Rect(2960, 340, 100, 18),
    pygame.Rect(3100, 250, 120, 18),
    pygame.Rect(3260, 370, 140, 18),
]

COIN_RECTS_INIT = [
    (250, 370), (420, 290), (560, 210), (740, 280),
    (900, 370), (1080, 280), (1210, 190), (1400, 270),
    (1540, 370), (1700, 270), (1840, 180), (2020, 280),
    (2180, 370), (2340, 270), (2490, 180), (2660, 290),
    (2820, 200), (3000, 310), (3140, 220), (3300, 340),
    (600, 470), (1200, 470), (1800, 470), (2400, 470), (3000, 470),
]

SPIKES_INIT = [
    (460, 488), (900, 488), (1300, 488), (1750, 488),
    (2100, 488), (2550, 488), (2900, 488), (3200, 488),
]

GOAL_POS = (3450, 390)


def show_screen(title, subtitle, score=None):
    screen.fill(BLACK)
    msg = font_large.render(title, True, WHITE)
    sub = font_small.render(subtitle, True, GRAY)
    screen.blit(msg, msg.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50)))
    screen.blit(sub, sub.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 20)))
    if score is not None:
        sc = font_med.render(f"Münzen: {score}", True, COIN_COLOR)
        screen.blit(sc, sc.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 70)))
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()


def draw_player(surf, rx, ry, facing):
    # Körper
    pygame.draw.rect(surf, PLAYER_COLOR, (rx, ry, 32, 40), border_radius=6)
    # Augen
    ex = rx + 20 if facing == 1 else rx + 6
    pygame.draw.circle(surf, PLAYER_EYE, (ex, ry + 12), 5)
    pygame.draw.circle(surf, BLACK, (ex, ry + 12), 2)
    # Beine (zwei Rechtecke)
    pygame.draw.rect(surf, (40, 100, 200), (rx + 4, ry + 34, 10, 10), border_radius=3)
    pygame.draw.rect(surf, (40, 100, 200), (rx + 18, ry + 34, 10, 10), border_radius=3)


def draw_platform(surf, r, cam_x):
    rx = r.x - cam_x
    if rx + r.width < 0 or rx > SCREEN_WIDTH:
        return
    # Seite
    pygame.draw.rect(surf, PLATFORM_COLOR, (rx, r.y, r.width, r.height))
    # Grasdeck
    pygame.draw.rect(surf, PLATFORM_TOP, (rx, r.y, r.width, 6))


def draw_coin(surf, x, y):
    pygame.draw.circle(surf, COIN_COLOR, (x, y), 10)
    pygame.draw.circle(surf, (255, 240, 100), (x, y), 6)


def draw_spike(surf, x, y):
    pygame.draw.polygon(surf, SPIKE_COLOR, [(x, y + 12), (x + 8, y), (x + 16, y + 12)])


def draw_goal(surf, x, y):
    # Stange
    pygame.draw.rect(surf, GRAY, (x, y - 60, 6, 70))
    # Flagge
    pygame.draw.polygon(surf, GOAL_COLOR, [(x + 6, y - 60), (x + 36, y - 45), (x + 6, y - 30)])


def main():
    show_screen("Plattformspiel", "ENTER zum Starten  |  ESC Beenden")

    while True:
        # Spielzustand
        player = pygame.Rect(60, 440, 32, 40)
        vel_y = 0
        on_ground = False
        facing = 1
        cam_x = 0
        coins = [pygame.Rect(cx, cy, 20, 20) for cx, cy in COIN_RECTS_INIT]
        spikes = [pygame.Rect(sx, sy, 16, 12) for sx, sy in SPIKES_INIT]
        goal_rect = pygame.Rect(GOAL_POS[0], GOAL_POS[1] - 60, 36, 70)
        score = 0
        lives = 3
        game_over = False
        won = False

        def respawn():
            nonlocal vel_y, on_ground
            player.x, player.y = 60, 440
            vel_y = 0
            on_ground = False

        while not game_over:
            clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    if event.key in (pygame.K_SPACE, pygame.K_UP, pygame.K_w) and on_ground:
                        vel_y = JUMP_FORCE
                        on_ground = False

            keys = pygame.key.get_pressed()
            dx = 0
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                dx = -PLAYER_SPEED
                facing = -1
            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                dx = PLAYER_SPEED
                facing = 1

            # Horizontale Bewegung
            player.x += dx
            player.x = max(0, min(player.x, WORLD_WIDTH - player.width))

            # Horizontale Plattform-Kollision
            for plat in PLATFORMS:
                if player.colliderect(plat):
                    if dx > 0:
                        player.right = plat.left
                    elif dx < 0:
                        player.left = plat.right

            # Schwerkraft
            vel_y += GRAVITY
            if vel_y > 18:
                vel_y = 18
            player.y += vel_y
            on_ground = False

            # Vertikale Plattform-Kollision
            for plat in PLATFORMS:
                if player.colliderect(plat):
                    if vel_y > 0:
                        player.bottom = plat.top
                        vel_y = 0
                        on_ground = True
                    elif vel_y < 0:
                        player.top = plat.bottom
                        vel_y = 0

            # Münzen einsammeln
            for c in coins[:]:
                if player.colliderect(c):
                    coins.remove(c)
                    score += 1

            # Stacheln
            for s in spikes:
                if player.colliderect(s):
                    lives -= 1
                    respawn()
                    if lives <= 0:
                        game_over = True
                    break

            # Aus dem Bild gefallen
            if player.top > SCREEN_HEIGHT + 50:
                lives -= 1
                respawn()
                if lives <= 0:
                    game_over = True

            # Ziel erreicht
            if player.colliderect(goal_rect):
                won = True
                game_over = True

            # Kamera
            cam_x = player.centerx - SCREEN_WIDTH // 3
            cam_x = max(0, min(cam_x, WORLD_WIDTH - SCREEN_WIDTH))

            # --- Zeichnen ---
            screen.fill(SKY)

            # Hintergrund-Dekorations-Hügel
            for hx in range(0, WORLD_WIDTH, 300):
                sx = hx - cam_x
                pygame.draw.ellipse(screen, (40, 100, 50), (sx, 390, 200, 120))

            # Plattformen
            for plat in PLATFORMS:
                draw_platform(screen, plat, cam_x)

            # Ziel
            draw_goal(screen, GOAL_POS[0] - cam_x, GOAL_POS[1])

            # Münzen
            for c in coins:
                draw_coin(screen, c.x - cam_x + 10, c.y + 10)

            # Stacheln
            for s in spikes:
                draw_spike(screen, s.x - cam_x, s.y)

            # Spieler
            draw_player(screen, player.x - cam_x, player.y, facing)

            # HUD
            hud_score = font_small.render(f"Münzen: {score}/{len(COIN_RECTS_INIT)}", True, HUD_COLOR)
            hud_lives = font_small.render(f"Leben: {'♥ ' * lives}", True, (220, 60, 60))
            screen.blit(hud_score, (10, 10))
            screen.blit(hud_lives, (SCREEN_WIDTH - 180, 10))

            ctrl = font_small.render("←→ / WASD bewegen   SPACE/↑ springen", True, GRAY)
            screen.blit(ctrl, ctrl.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 18)))

            pygame.display.flip()

        if won:
            show_screen("Gewonnen!", f"ENTER für neues Spiel  |  ESC Beenden", score)
        else:
            show_screen("Game Over", "ENTER für neues Spiel  |  ESC Beenden", score)


if __name__ == "__main__":
    main()
