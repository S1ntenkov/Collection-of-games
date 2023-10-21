import pygame
import random

WIDTH = 498
HEIGHT = 278
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
pygame.display.set_caption("Game Launcher")
clock = pygame.time.Clock()

#Гифка
background = pygame.image.load('pixel_art_background.gif').convert()
background = pygame.transform.smoothscale(background, screen.get_size())
# Рендеринг
#screen.fill(BLACK)
screen.blit(background, (0, 0))
# после отрисовки всего, переворачиваем экран
pygame.display.flip()
# Цикл игры
running = True
while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    # Ввод процесса (события)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
pygame.quit()