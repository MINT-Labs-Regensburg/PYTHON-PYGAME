import pygame
import sys
import random

pygame.init()

# Konstanten
CELL_SIZE = 20
COLS = 30
ROWS = 25
SCREEN_WIDTH = COLS * CELL_SIZE
SCREEN_HEIGHT = ROWS * CELL_SIZE
FPS = 5

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 200, 50)
DARK_GREEN = (0, 140, 30)
RED = (220, 40, 40)
GRAY = (50, 50, 50)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()

font_large = pygame.font.SysFont("monospace", 64, bold=True)
font_small = pygame.font.SysFont("monospace", 26)


def random_food(snake):
    while True:
        pos = (random.randint(0, COLS - 1), random.randint(0, ROWS - 1))
        if pos not in snake:
            return pos


def draw_grid():
    for x in range(0, SCREEN_WIDTH, CELL_SIZE):
        pygame.draw.line(screen, GRAY, (x, 0), (x, SCREEN_HEIGHT))
    for y in range(0, SCREEN_HEIGHT, CELL_SIZE):
        pygame.draw.line(screen, GRAY, (0, y), (SCREEN_WIDTH, y))


def draw_snake(snake):
    for i, (cx, cy) in enumerate(snake):
        color = DARK_GREEN if i == 0 else GREEN
        rect = pygame.Rect(cx * CELL_SIZE + 1, cy * CELL_SIZE + 1, CELL_SIZE - 2, CELL_SIZE - 2)
        pygame.draw.rect(screen, color, rect, border_radius=4)


def draw_food(food):
    cx, cy = food
    rect = pygame.Rect(cx * CELL_SIZE + 2, cy * CELL_SIZE + 2, CELL_SIZE - 4, CELL_SIZE - 4)
    pygame.draw.ellipse(screen, RED, rect)


def show_screen(title, subtitle):
    screen.fill(BLACK)
    msg = font_large.render(title, True, WHITE)
    sub = font_small.render(subtitle, True, GRAY)
    screen.blit(msg, msg.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 40)))
    screen.blit(sub, sub.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 40)))
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


def main():
    show_screen("SNAKE", "ENTER zum Starten  |  ESC Beenden")

    while True:
        # Spielzustand initialisieren
        start_x, start_y = COLS // 2, ROWS // 2
        snake = [(start_x, start_y), (start_x - 1, start_y), (start_x - 2, start_y)]
        direction = (1, 0)
        next_direction = direction
        food = random_food(snake)
        score = 0
        game_over = False

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
                    elif event.key == pygame.K_UP and direction != (0, 1):
                        next_direction = (0, -1)
                    elif event.key == pygame.K_DOWN and direction != (0, -1):
                        next_direction = (0, 1)
                    elif event.key == pygame.K_LEFT and direction != (1, 0):
                        next_direction = (-1, 0)
                    elif event.key == pygame.K_RIGHT and direction != (-1, 0):
                        next_direction = (1, 0)

            direction = next_direction
            head = (snake[0][0] + direction[0], snake[0][1] + direction[1])

            # Wand-Kollision
            if not (0 <= head[0] < COLS and 0 <= head[1] < ROWS):
                game_over = True
                break

            # Selbst-Kollision
            if head in snake:
                game_over = True
                break

            snake.insert(0, head)

            if head == food:
                score += 1
                food = random_food(snake)
            else:
                snake.pop()

            # Zeichnen
            screen.fill(BLACK)
            draw_grid()
            draw_food(food)
            draw_snake(snake)

            score_surf = font_small.render(f"Punkte: {score}", True, WHITE)
            screen.blit(score_surf, (10, 8))

            pygame.display.flip()

        show_screen("Game Over", f"Punkte: {score}  |  ENTER für neues Spiel")


if __name__ == "__main__":
    main()
