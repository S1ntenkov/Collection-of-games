import pygame
from game import Game

WIDTH = 400
HEIGHT = 800
FPS = 60
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
# Рендеринг
screen.fill(BLACK)
# после отрисовки всего, переворачиваем экран
pygame.display.flip()
# Цикл игры
game = Game()
running = True
while running:
    # Держим цикл на правильной скорости

    # Ввод процесса (события)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.type == pygame.K_LEFT:
    # рисуем сетку
    screen.fill(BLACK)
    game.draw(screen)
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()