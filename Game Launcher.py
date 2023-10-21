import pygame
import os
import random
pygame.init()
pygame.mixer.init()
WIDTH = 498
HEIGHT = 278
FPS = 30
# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
#Звук кнопки
pygame.mixer.music.load("minecraft_click.mp3")
#Прямоугольники для кнопок
rect1 = pygame.Rect((150, 60, 200, 50))
rect2 = pygame.Rect((150, 140, 200, 50))
# Создаем игру и окно

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game Launcher")
clock = pygame.time.Clock()
font = pygame.font.SysFont('Comic Sans MS', 30)
objects = []
class Button():
    def __init__(self, x, y, WIDTH, HEIGHT, buttonText='Button', onclickFunction=None, onePress=False):
        self.x = x
        self.y = y
        self.width = WIDTH
        self.height = HEIGHT
        self.onclickFunction = onclickFunction
        self.onePress = onePress
        self.alreadyPressed = False

        self.fillColors = {
            'normal': '#6e6e6e',
            'hover': '#444444',
            'pressed': '#333333',
        }
        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.buttonSurf = font.render(buttonText, True, WHITE)
        objects.append(self)

    def process(self):
        mousePos = pygame.mouse.get_pos()
        self.buttonSurface.fill(self.fillColors['normal'])
        if self.buttonRect.collidepoint(mousePos):
            self.buttonSurface.fill(self.fillColors['hover'])
            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                self.buttonSurface.fill(self.fillColors['pressed'])
                pygame.mixer.music.play(1,0.4)
                if self.onePress:
                    self.onclickFunction()
                elif not self.alreadyPressed:
                    self.onclickFunction()
                    self.alreadyPressed = True
            else:
                self.alreadyPressed = False
        self.buttonSurface.blit(self.buttonSurf, [
            self.buttonRect.width / 2 - self.buttonSurf.get_rect().width / 2,
            self.buttonRect.height / 2 - self.buttonSurf.get_rect().height / 2
        ])
        screen.blit(self.buttonSurface, self.buttonRect)
#Функция определяющая действие после нажатия кнопки
def Button1():
    os.system('python SnakeGame.py')
def Button2():
    os.system('python TetrisGame.py')
Button(150, 60, 200, 50, 'Snake game', Button1)
Button(150, 140, 200, 50, 'Tetris game', Button2)
#Гифка
background = pygame.image.load('pixel_art_background.gif').convert()
background = pygame.transform.smoothscale(background, screen.get_size())
# Рендеринг
#screen.fill(BLACK)

screen.blit(background, (0, 0))
# после отрисовки всего, переворачиваем экран

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
    for object in objects:
        object.process()
    # Рисую прямоугольники
    pygame.draw.rect(screen, BLACK, rect1, 2)
    pygame.draw.rect(screen, BLACK, rect2, 2)
    pygame.display.flip()
pygame.quit()