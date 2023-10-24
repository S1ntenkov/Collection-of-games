import pygame
import random
from pygame.math import Vector2



pygame.init()
#pygame.mixer.init()
#Звук поедания яблока
pygame.mixer.music.load("ukus-yabloka-korotkiy.mp3")
rect1 = pygame.Rect((20,20, 380, 400))

class SNAKE:

    def __init__(self):
        self.body = [Vector2(6,10),Vector2(7,10),Vector2(8,10)]
        self.direction = Vector2(1,0)

        # Текстуры головы змеи
        self.head = pygame.image.load("snakehead_right.png").convert_alpha()
        self.head_up = pygame.image.load("snakehead_up.png").convert_alpha()
        self.head_left = pygame.image.load("snakehead_left.png").convert_alpha()
        self.head_right = pygame.image.load("snakehead_right.png").convert_alpha()
        self.head_down = pygame.image.load("snakehead_down.png").convert_alpha()
        # Текстуры хвоста змеи
        self.tail = pygame.image.load("snaketail_right.png").convert_alpha()
        self.tail_up = pygame.image.load("snaketail_up.png").convert_alpha()
        self.tail_left = pygame.image.load("snaketail_left.png").convert_alpha()
        self.tail_right = pygame.image.load("snaketail_right.png").convert_alpha()
        self.tail_down = pygame.image.load("snaketail_down.png").convert_alpha()
        # Текстуры сгибов змеи
        self.corner_rup = pygame.image.load("snake-corner_rightup.png").convert_alpha()
        self.corner_lup = pygame.image.load("snake-corner_leftup.png").convert_alpha()
        self.corner_ldown = pygame.image.load("snake-corner_leftdown.png").convert_alpha()
        self.corner_rdown = pygame.image.load("snake-corner_rightdown.png").convert_alpha()

    def draw_snake(self):
        self.update_head_graphics()
        self.update_tail_graphics()
        for index,block in enumerate(self.body):
            x_pos = int(block.x*cell_size)
            y_pos = int(block.y*cell_size)
            block_rect = pygame.Rect(x_pos,y_pos,cell_size,cell_size)
            if index == 0:
                screen.blit(self.head,block_rect)
            elif index == len(self.body)-1:
                screen.blit(self.tail,block_rect)
            else:
                previous_block = self.body[index+1]-block
                next_block = self.body[index-1] - block
                if previous_block.x == next_block.x:
                    screen.blit(pygame.transform.rotate(snakeskin, 90),block_rect)
                elif previous_block.y == next_block.y:
                    screen.blit(pygame.transform.rotate(snakeskin, 0),block_rect)
                else:
                    if previous_block.x == -1 and next_block.y==-1 or previous_block.y == -1 and next_block.x==-1:
                        screen.blit(self.corner_lup,block_rect)
                    elif previous_block.x == -1 and next_block.y==1 or previous_block.y == 1 and next_block.x==-1:
                        screen.blit(self.corner_rdown,block_rect)
                    elif previous_block.x == 1 and next_block.y==-1 or previous_block.y == -1 and next_block.x==1:
                        screen.blit(self.corner_ldown,block_rect)
                    elif previous_block.x == 1 and next_block.y==1 or previous_block.y == 1 and next_block.x==1:
                        screen.blit(self.corner_rup,block_rect)
        #fruit_rect = pygame.Rect(self.body ,cell_size, cell_size*2)
    def update_head_graphics(self):
        head_relation = self.body[1]-self.body[0]
        if head_relation == Vector2(1,0): self.head = self.head_left
        elif head_relation == Vector2(-1, 0): self.head = self.head_right
        elif head_relation == Vector2(0, 1):self.head = self.head_up
        elif head_relation == Vector2(0, -1):self.head =self.head_down
    def update_tail_graphics(self):
        tail_relation = self.body[-2]-self.body[-1]
        if tail_relation == Vector2(1,0): self.tail = self.tail_right
        elif tail_relation == Vector2(-1, 0): self.tail = self.tail_left
        elif tail_relation == Vector2(0, 1):self.tail = self.tail_down
        elif tail_relation == Vector2(0, -1):self.tail =self.tail_up

    def move_snake(self):
        body_copy = self.body[:-1]
        body_copy.insert(0,body_copy[0]+self.direction)
        self.body = body_copy[:]





class FRUIT:
    def __init__(self):
        self.x= random.randint(1,cell_number-1)
        self.y= random.randint(1,cell_number-1)
        self.pos = (Vector2(self.x*cell_size,self.y*cell_size))
    def draw_fruit(self):
        fruit_rect = pygame.Rect(self.pos.x,self.pos.y,cell_size,cell_size)
        screen.blit(apple, fruit_rect)

#cell_size = 40
#cell_number = 20
cell_size = 20
cell_number = 20

#screen = pygame.display.set_mode((cell_size*cell_number, cell_number*cell_size))
screen = pygame.display.set_mode((420,500))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()
#Текстура яблока
apple= pygame.image.load('текстура-яблока.png').convert()

#Кожа змеи
snakeskin= pygame.image.load("snakeskin.png").convert_alpha() #.convert_alpha() для прозрачности
pygame.transform.rotate(snakeskin, 180)


pygame.display.flip()

running = True
fruit = FRUIT()
snake = SNAKE()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,150)


player_score = "0"
high_score_file = open("high_score.txt", "rt")
high_score = high_score_file.read()

print(high_score,'high score')

font = pygame.font.SysFont('Unispace', 80)
font2 = pygame.font.SysFont('Unispace', 40)
img = font.render(player_score, True, "white")
img2= font2.render("high score: "+high_score, True, "white")

default_angle = 0

while running:
    for event in pygame.event.get():

        # check for closing window
        if event.type == pygame.QUIT:
            running = False
        if event.type == SCREEN_UPDATE:
            snake.move_snake()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake.direction.y!=1:
                snake.direction=Vector2(0,-1)
            if event.key == pygame.K_DOWN and snake.direction.y!=-1:
                snake.direction=Vector2(0,+1)
            if event.key == pygame.K_RIGHT and snake.direction.x!=-1:
                snake.direction=Vector2(+1,0)
            if event.key == pygame.K_LEFT and snake.direction.x!=1:
                snake.direction=Vector2(-1,0)

        if snake.body[0] == fruit.pos/cell_size:
            fruit.pos=Vector2(random.randint(1,cell_number-1)*cell_size,random.randint(1,cell_number-1)*cell_size)
            snake.body.append(Vector2(fruit.pos/cell_size))
            pygame.mixer.music.play(1)
            print("ate an apple")

            player_score=str(int(player_score)+1)
            img = font.render(player_score, True, "white")


        if snake.body[0][0]<1 or snake.body[0][0]>19 or snake.body[0][1]<1 or snake.body[0][1]>20:
            running=False
            print("Watch your step!")

            if player_score > high_score:

                high_score = high_score.replace(str(high_score), str(player_score))
                high_score_file = open("high_score.txt", "wt")
                high_score_file.write(high_score)



        for body in snake.body[3:]:

            if snake.body[0]==body:
                print(body, snake.body[0])
                running=False
                print("Ate yourself!")
                if player_score > high_score:
                    high_score = high_score.replace(str(high_score), str(player_score))
                    high_score_file = open("high_score.txt", "wt")
                    high_score_file.write(high_score)




    #screen.fill((255, 215, 70))
    screen.fill((0,0,0))
    screen.blit(img, (30, 430))
    screen.blit(img2, (200, 450))
    fruit.draw_fruit()
    snake.draw_snake()
    pygame.draw.rect(screen, ((255, 255, 255)), rect1, 2)



    #print([fruit.x,fruit.y])

    #logic end
    pygame.display.update()
    clock.tick(60)

pygame.quit()