import pygame
from grid import Grid
import random

WIDTH = 400
HEIGHT = 800
FPS = 30
# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tetris Game")
clock = pygame.time.Clock()
#создаем сетку
game_grid = Grid()
game_grid.print_grid()
# Рендеринг
screen.fill(BLACK)
# после отрисовки всего, переворачиваем экран
pygame.display.flip()
# Цикл игры
running = True
while running:
    # Держим цикл на правильной скорости

    # Ввод процесса (события)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
    # рисуем сетку
    game_grid.draw(screen)

    pygame.display.update()
    clock.tick(FPS)
pygame.quit()