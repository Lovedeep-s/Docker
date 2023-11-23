import pygame
import numpy as np

gsize = 50
csize = 10
WIDTH, HEIGHT = gsize * csize, gsize * csize
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def new_grid():
    return np.random.choice([0, 1], size=(gsize, gsize))

def count(grid, x, y):
    neighbors = [(x+i, y+j) 
                 for i in [-1, 0, 1] 
                    for j in [-1, 0, 1] 
                        if not (i == 0 and j == 0)
                ]
    lneighbors = sum(1 for i, j in neighbors 
                            if 0 <= i < gsize and 0 <= j < gsize and grid[i, j] == 1
                        )
    return lneighbors

def ugrid(grid):
    new_grid = np.copy(grid)
    for i in range(gsize):
        for j in range(gsize):
            lneighbors = count(grid, i, j)
            
            if grid[i, j] == 1:
                
                if lneighbors < 2 or lneighbors > 3:
                    new_grid[i, j] = 0
            else:
                
                if lneighbors == 3:
                    new_grid[i, j] = 1

    return new_grid

def draw_grid(screen, grid):
    for i in range(gsize):
        for j in range(gsize):
            color = WHITE if grid[i, j] == 1 else BLACK
            pygame.draw.rect(screen, color, (j * csize, i * csize, csize, csize))



pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Lovedeep's Game")
clock = pygame.time.Clock()
grid = new_grid()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    screen.fill(BLACK)
    draw_grid(screen, grid)
    grid = ugrid(grid)

    pygame.display.flip()
    clock.tick(5)  # Adjust the speed of the simulation


