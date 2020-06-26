import pygame, random
from copy import deepcopy

pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Game Of Life")

ROWS = 160
COLS = 160
side = 5
grid = [[random.randint(0, 1) for j in range(COLS)] for i in range(ROWS)]

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ALIVE = 1
DEAD = 0


def print_grid():
    for i in range(ROWS):
        for j in range(COLS):
            color = {ALIVE: WHITE, DEAD: BLACK}[grid[i][j]]
            pygame.draw.rect(screen, color, (i*side, j*side, side-1, side-1), 0)


def count_neighbours(x, y, grid):
    neighbours = -grid[x][y]
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            neighbours += grid[x+i][y+j]
    return neighbours


def update_grid():
    prev_grid = deepcopy(grid)
    for i in range(1, ROWS-1):
        for j in range(1, COLS-1):
            alive_neighbours = count_neighbours(i, j, prev_grid)
            status = grid[i][j]
            if status == DEAD and alive_neighbours == 3:
                grid[i][j] = ALIVE
            elif status == ALIVE and not alive_neighbours in [2, 3]:
                grid[i][j] = DEAD

#--------------------------

running = True
while running:

    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print_grid()
            update_grid()
            pygame.display.update()

