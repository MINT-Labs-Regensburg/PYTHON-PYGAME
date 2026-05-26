import pygame
import sys
import random

pygame.init()

# Konstanten
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 30

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 230, 80)
RED = (220, 40, 40)
CYAN = (0, 220, 220)
YELLOW = (240, 220, 0)
GRAY = (60, 60, 60)
DARK_GREEN = (0, 120, 40)

PLAYER_SPEED = 5
BULLET_SPEED = 8
ENEMY_BULLET_SPEED = 4
ENEMY_COLS = 10
ENEMY_ROWS = 4
ENEMY_H_GAP = 60
ENEMY_V_GAP = 50
ENEMY_DROP = 20
ENEMY_MOVE_INTERVAL = 600  # ms

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Invaders")
clock = pygame.time.Clock()

font_large = pygame.font.SysFont("monospace", 64, bold=True)
font_med = pygame.font.SysFont("monospace", 32, bold=True)
font_small = pygame.font.SysFont("monospace", 24)


# --- Zeichenfunktionen ---

def draw_player(surf, x, y):
    # Rumpf
    pygame.draw.rect(surf, GREEN, (x + 18, y + 10, 14, 20))
    # Kanzel
    pygame.draw.polygon(surf, GREEN, [(x + 25, y), (x + 18, y + 12), (x + 32, y + 12)])
    # Flügel links
    pygame.draw.polygon(surf, GREEN, [(x, y + 30), (x + 20, y + 15), (x + 20, y + 30)])
    # Flügel rechts
    pygame.draw.polygon(surf, GREEN, [(x + 50, y + 30), (x + 30, y + 15), (x + 30, y + 30)])


def draw_enemy(surf, x, y, row):
    colors = [RED, CYAN, YELLOW, WHITE]
    color = colors[row % len(colors)]
    # Körper
    pygame.draw.rect(surf, color, (x + 8, y + 8, 24, 16), border_radius=4)
    # Kopf
    pygame.draw.rect(surf, color, (x + 12, y + 2, 16, 10), border_radius=3)
    # Augen
    pygame.draw.circle(surf, BLACK, (x + 16, y + 7), 3)
    pygame.draw.circle(surf, BLACK, (x + 24, y + 7), 3)
    # Tentakel links
    pygame.draw.line(surf, color, (x + 10, y + 24), (x + 4, y + 32), 2)
    pygame.draw.line(surf, color, (x + 15, y + 24), (x + 12, y + 34), 2)
    # Tentakel rechts
    pygame.draw.line(surf, color, (x + 30, y + 24), (x + 36, y + 32), 2)
    pygame.draw.line(surf, color, (x + 25, y + 24), (x + 28, y + 34), 2)


def draw_bunker(surf, bunker_rects):
    for r in bunker_rects:
        pygame.draw.rect(surf, DARK_GREEN, r)


def show_screen(title, subtitle, score=None):
    screen.fill(BLACK)
    msg = font_large.render(title, True, WHITE)
    sub = font_small.render(subtitle, True, GRAY)
    screen.blit(msg, msg.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50)))
    screen.blit(sub, sub.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 20)))
    if score is not None:
        sc = font_med.render(f"Punkte: {score}", True, YELLOW)
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


def make_bunkers():
    bunkers = []
    positions = [130, 280, 430, 580]
    for bx in positions:
        group = []
        for row in range(4):
            for col in range(6):
                r = pygame.Rect(bx + col * 12, 460 + row * 10, 10, 8)
                group.append(r)
        bunkers.append(group)
    return bunkers


def make_enemies():
    enemies = []
    start_x = 60
    start_y = 60
    for row in range(ENEMY_ROWS):
        for col in range(ENEMY_COLS):
            x = start_x + col * ENEMY_H_GAP
            y = start_y + row * ENEMY_V_GAP
            enemies.append({"rect": pygame.Rect(x, y, 40, 36), "row": row, "alive": True})
    return enemies


def main():
    show_screen("SPACE INVADERS", "ENTER zum Starten  |  ESC Beenden")

    while True:
        # Spielzustand
        player = pygame.Rect(SCREEN_WIDTH // 2 - 25, SCREEN_HEIGHT - 60, 50, 30)
        player_bullets = []
        enemy_bullets = []
        enemies = make_enemies()
        bunkers = make_bunkers()
        score = 0
        lives = 3
        enemy_dir = 1  # 1=rechts, -1=links
        last_move_time = pygame.time.get_ticks()
        enemy_shoot_timer = 0
        game_over = False
        won = False

        while not game_over:
            dt = clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    if event.key == pygame.K_SPACE:
                        if len(player_bullets) < 3:
                            bx = player.centerx - 3
                            by = player.top - 10
                            player_bullets.append(pygame.Rect(bx, by, 6, 14))

            # Spieler bewegen
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and player.left > 0:
                player.x -= PLAYER_SPEED
            if keys[pygame.K_RIGHT] and player.right < SCREEN_WIDTH:
                player.x += PLAYER_SPEED

            # Spieler-Schüsse bewegen
            for b in player_bullets[:]:
                b.y -= BULLET_SPEED
                if b.bottom < 0:
                    player_bullets.remove(b)

            # Gegner-Schüsse bewegen
            for b in enemy_bullets[:]:
                b.y += ENEMY_BULLET_SPEED
                if b.top > SCREEN_HEIGHT:
                    enemy_bullets.remove(b)

            # Gegner bewegen
            now = pygame.time.get_ticks()
            alive_enemies = [e for e in enemies if e["alive"]]
            move_interval = max(80, ENEMY_MOVE_INTERVAL - (40 - len(alive_enemies)) * 13)
            if now - last_move_time > move_interval:
                last_move_time = now
                # Rand prüfen
                hit_wall = False
                for e in alive_enemies:
                    if (enemy_dir == 1 and e["rect"].right >= SCREEN_WIDTH - 10) or \
                       (enemy_dir == -1 and e["rect"].left <= 10):
                        hit_wall = True
                        break
                if hit_wall:
                    for e in alive_enemies:
                        e["rect"].y += ENEMY_DROP
                    enemy_dir *= -1
                else:
                    for e in alive_enemies:
                        e["rect"].x += enemy_dir * 20

            # Gegner schießen
            enemy_shoot_timer += dt
            if enemy_shoot_timer > 800 and alive_enemies:
                enemy_shoot_timer = 0
                shooter = random.choice(alive_enemies)
                bx = shooter["rect"].centerx - 3
                by = shooter["rect"].bottom
                enemy_bullets.append(pygame.Rect(bx, by, 6, 14))

            # Kollision: Spieler-Schuss trifft Gegner
            for b in player_bullets[:]:
                for e in alive_enemies:
                    if b.colliderect(e["rect"]):
                        e["alive"] = False
                        if b in player_bullets:
                            player_bullets.remove(b)
                        score += (ENEMY_ROWS - e["row"]) * 10
                        break

            # Kollision: Schüsse treffen Bunker
            all_bunker_rects = [r for group in bunkers for r in group]
            for b in player_bullets[:]:
                for r in all_bunker_rects[:]:
                    if b.colliderect(r):
                        for group in bunkers:
                            if r in group:
                                group.remove(r)
                        if b in player_bullets:
                            player_bullets.remove(b)
                        break
            for b in enemy_bullets[:]:
                for r in all_bunker_rects[:]:
                    if b.colliderect(r):
                        for group in bunkers:
                            if r in group:
                                group.remove(r)
                        if b in enemy_bullets:
                            enemy_bullets.remove(b)
                        break

            # Kollision: Gegner-Schuss trifft Spieler
            for b in enemy_bullets[:]:
                if b.colliderect(player):
                    enemy_bullets.remove(b)
                    lives -= 1
                    if lives <= 0:
                        game_over = True
                    break

            # Gegner erreichen Spieler-Linie
            for e in alive_enemies:
                if e["rect"].bottom >= player.top:
                    game_over = True
                    break

            # Alle Gegner besiegt
            if not alive_enemies:
                won = True
                game_over = True

            # --- Zeichnen ---
            screen.fill(BLACK)

            # Boden
            pygame.draw.line(screen, GREEN, (0, SCREEN_HEIGHT - 25), (SCREEN_WIDTH, SCREEN_HEIGHT - 25), 2)

            # Bunker
            for group in bunkers:
                draw_bunker(screen, group)

            # Spieler
            draw_player(screen, player.x, player.y)

            # Gegner
            for e in enemies:
                if e["alive"]:
                    draw_enemy(screen, e["rect"].x, e["rect"].y, e["row"])

            # Schüsse
            for b in player_bullets:
                pygame.draw.rect(screen, YELLOW, b, border_radius=3)
            for b in enemy_bullets:
                pygame.draw.rect(screen, RED, b, border_radius=3)

            # HUD
            score_surf = font_small.render(f"Punkte: {score}", True, WHITE)
            lives_surf = font_small.render(f"Leben: {'♥ ' * lives}", True, RED)
            screen.blit(score_surf, (10, 8))
            screen.blit(lives_surf, (SCREEN_WIDTH - 160, 8))

            pygame.display.flip()

        if won:
            show_screen("Du gewinnst!", "ENTER für neues Spiel  |  ESC Beenden", score)
        else:
            show_screen("Game Over", "ENTER für neues Spiel  |  ESC Beenden", score)


if __name__ == "__main__":
    main()
