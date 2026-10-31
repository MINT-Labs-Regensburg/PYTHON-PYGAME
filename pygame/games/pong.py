import pygame
import sys

pygame.init()

# Konstanten
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (50, 50, 50)

PADDLE_WIDTH = 15
PADDLE_HEIGHT = 90
PADDLE_SPEED = 6

BALL_SIZE = 15
BALL_SPEED_X = 5
BALL_SPEED_Y = 4

WINNING_SCORE = 10

# Screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pong - Zwei Spieler")
clock = pygame.time.Clock()

font_large = pygame.font.SysFont("monospace", 72, bold=True)
font_small = pygame.font.SysFont("monospace", 28)


def reset_ball(dx=1):
    ball = pygame.Rect(
        SCREEN_WIDTH // 2 - BALL_SIZE // 2,
        SCREEN_HEIGHT // 2 - BALL_SIZE // 2,
        BALL_SIZE,
        BALL_SIZE,
    )
    ball_vel = [BALL_SPEED_X * dx, BALL_SPEED_Y]
    return ball, ball_vel


def draw_dashed_line():
    dash_height = 20
    gap = 10
    x = SCREEN_WIDTH // 2 - 2
    for y in range(0, SCREEN_HEIGHT, dash_height + gap):
        pygame.draw.rect(screen, GRAY, (x, y, 4, dash_height))


def show_winner(winner):
    screen.fill(BLACK)
    msg = font_large.render(f"Spieler {winner} gewinnt!", True, WHITE)
    sub = font_small.render("Drücke ENTER für neues Spiel  oder  ESC zum Beenden", True, GRAY)
    screen.blit(msg, msg.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50)))
    screen.blit(sub, sub.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 40)))
    pygame.display.flip()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    waiting = False
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()


def main():
    score = [0, 0]
    paddle1 = pygame.Rect(20, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
    paddle2 = pygame.Rect(
        SCREEN_WIDTH - 20 - PADDLE_WIDTH,
        SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2,
        PADDLE_WIDTH,
        PADDLE_HEIGHT,
    )
    ball, ball_vel = reset_ball()

    while True:
        clock.tick(FPS)

        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

        # Paddle-Bewegung
        keys = pygame.key.get_pressed()

        # Spieler 1: W / S
        if keys[pygame.K_w] and paddle1.top > 0:
            paddle1.y -= PADDLE_SPEED
        if keys[pygame.K_s] and paddle1.bottom < SCREEN_HEIGHT:
            paddle1.y += PADDLE_SPEED

        # Spieler 2: Pfeiltasten Oben / Unten
        if keys[pygame.K_UP] and paddle2.top > 0:
            paddle2.y -= PADDLE_SPEED
        if keys[pygame.K_DOWN] and paddle2.bottom < SCREEN_HEIGHT:
            paddle2.y += PADDLE_SPEED

        # Ball bewegen
        ball.x += ball_vel[0]
        ball.y += ball_vel[1]

        # Oben / Unten abprallen
        if ball.top <= 0:
            ball.top = 0
            ball_vel[1] *= -1
        if ball.bottom >= SCREEN_HEIGHT:
            ball.bottom = SCREEN_HEIGHT
            ball_vel[1] *= -1

        # Paddle-Kollision
        if ball.colliderect(paddle1) and ball_vel[0] < 0:
            ball.left = paddle1.right
            ball_vel[0] *= -1
            # Einfluss der Paddle-Position auf Y-Richtung
            offset = (ball.centery - paddle1.centery) / (PADDLE_HEIGHT / 2)
            ball_vel[1] = int(offset * BALL_SPEED_Y * 1.5)
        if ball.colliderect(paddle2) and ball_vel[0] > 0:
            ball.right = paddle2.left
            ball_vel[0] *= -1
            offset = (ball.centery - paddle2.centery) / (PADDLE_HEIGHT / 2)
            ball_vel[1] = int(offset * BALL_SPEED_Y * 1.5)

        # Punkte
        if ball.left <= 0:
            score[1] += 1
            ball, ball_vel = reset_ball(dx=1)
        elif ball.right >= SCREEN_WIDTH:
            score[0] += 1
            ball, ball_vel = reset_ball(dx=-1)

        # Gewinner prüfen
        if score[0] >= WINNING_SCORE:
            show_winner(1)
            score = [0, 0]
            paddle1.y = SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2
            paddle2.y = SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2
            ball, ball_vel = reset_ball()
        elif score[1] >= WINNING_SCORE:
            show_winner(2)
            score = [0, 0]
            paddle1.y = SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2
            paddle2.y = SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2
            ball, ball_vel = reset_ball()

        # Zeichnen
        screen.fill(BLACK)
        draw_dashed_line()
        pygame.draw.rect(screen, WHITE, paddle1)
        pygame.draw.rect(screen, WHITE, paddle2)
        pygame.draw.ellipse(screen, WHITE, ball)

        # Punkte anzeigen
        score1_surf = font_large.render(str(score[0]), True, WHITE)
        score2_surf = font_large.render(str(score[1]), True, WHITE)
        screen.blit(score1_surf, score1_surf.get_rect(center=(SCREEN_WIDTH // 4, 60)))
        screen.blit(score2_surf, score2_surf.get_rect(center=(3 * SCREEN_WIDTH // 4, 60)))

        # Steuerung-Hinweis
        hint = font_small.render("Spieler 1: W/S      Spieler 2: ↑/↓", True, GRAY)
        screen.blit(hint, hint.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 20)))

        pygame.display.flip()


if __name__ == "__main__":
    main()
