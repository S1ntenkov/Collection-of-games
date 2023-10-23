import pygame,sys
from game import Game
from colors import Colors
#экранчик
pygame.init()
title_font = pygame.font.Font(None, 40)
score_surface = title_font.render("Счет", True, Colors.white)
next_surface = title_font.render("Следующий", True, Colors.white)
game_over_surface = title_font.render("Игра Завершена", True, Colors.white)
pygame.display.set_caption("Tetris")
score_rect = pygame.Rect(320, 55, 170, 60)
next_rect = pygame.Rect(320, 215, 170, 180)
screen = pygame.display.set_mode((560, 620))
clock = pygame.time.Clock()
game = Game()
#скорость падения
GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 220)
#цикл
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if game.game_over == True:
                game.game_over = False
                game.reset()
            if event.key == pygame.K_LEFT and game.game_over == False:
                game.move_left()
            if event.key == pygame.K_RIGHT and game.game_over == False:
                game.move_right()
            if event.key == pygame.K_DOWN and game.game_over == False:
                game.move_down()
                game.update_score(0, 1)
            if event.key == pygame.K_UP and game.game_over == False:
                game.rotate()
            if event.key == pygame.K_TAB and game.game_over == False:
                print(1)
        if event.type == GAME_UPDATE and game.game_over == False:
            game.move_down()
    #отображение
    score_value_surface = title_font.render(str(game.score), True, Colors.white)

    screen.fill(Colors.dark_blue)
    screen.blit(score_surface, (369, 20, 50, 50))
    screen.blit(next_surface, (318, 180, 50, 50))

    if game.game_over == True:
        screen.blit(game_over_surface, (320, 450, 50, 50))

    pygame.draw.rect(screen, Colors.light_blue, score_rect, 0, 10)
    screen.blit(score_value_surface, score_value_surface.get_rect(centerx = score_rect.centerx, 
        centery = score_rect.centery))
    pygame.draw.rect(screen, Colors.light_blue, next_rect, 0, 10)
    game.draw(screen)

    pygame.display.update()
    clock.tick(60)