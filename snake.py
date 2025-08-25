import pygame
import random
import sys

# initialize pygame
pygame.init()

# game window
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Clone")

# colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# snake & food
snake = [(100, 100), (90, 100), (80, 100)]
direction = (CELL_SIZE, 0)
food = (random.randrange(0, WIDTH // CELL_SIZE) * CELL_SIZE,
        random.randrange(0, HEIGHT // CELL_SIZE) * CELL_SIZE)

clock = pygame.time.Clock()

def draw_window():
    win.fill(BLACK)
    for x, y in snake:
        pygame.draw.rect(win, GREEN, (x, y, CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(win, RED, (food[0], food[1], CELL_SIZE, CELL_SIZE))
    pygame.display.update()

while True:
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and direction != (0, CELL_SIZE):
        direction = (0, -CELL_SIZE)
    if keys[pygame.K_DOWN] and direction != (0, -CELL_SIZE):
        direction = (0, CELL_SIZE)
    if keys[pygame.K_LEFT] and direction != (CELL_SIZE, 0):
        direction = (-CELL_SIZE, 0)
    if keys[pygame.K_RIGHT] and direction != (-CELL_SIZE, 0):
        direction = (CELL_SIZE, 0)

    # move snake
    new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
    snake.insert(0, new_head)

    # check food
    if snake[0] == food:
        food = (random.randrange(0, WIDTH // CELL_SIZE) * CELL_SIZE,
                random.randrange(0, HEIGHT // CELL_SIZE) * CELL_SIZE)
    else:
        snake.pop()

    # check collisions (walls)
    if (new_head[0] < 0 or new_head[0] >= WIDTH or
        new_head[1] < 0 or new_head[1] >= HEIGHT or
        new_head in snake[1:]):
        pygame.quit()
        sys.exit()

    draw_window()
