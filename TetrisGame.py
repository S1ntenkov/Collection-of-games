import pygame, sys
import random
from grid import Grid

WIDTH = 400
HEIGHT = 800
FPS = 45
DARK_BLUE = (44, 44, 100)
# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tetris Game")
clock = pygame.time.Clock()

# Цикл игры
running = True
game_grid = Grid()
game_grid.print_grid()

while running:
    pygame.display.update()
    clock.tick(FPS)
    # Ввод процесса (события)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
    screen.fill(DARK_BLUE)
    
pygame.quit()
sys.exit()