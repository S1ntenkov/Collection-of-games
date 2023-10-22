import pygame
import random
from pygame.math import Vector2



pygame.init()
#pygame.mixer.init()

class SNAKE:
    def __init__(self):
        self.body = [Vector2(5,10),Vector2(6,10),Vector2(7,10)]
        self.direction = Vector2(1,0)
    def draw_snake(self):

        for block in self.body:
            block_rect = pygame.Rect(block.x*cell_size,block.y*cell_size,cell_size,cell_size)
            pygame.draw.rect(screen, ("green"), block_rect)
        #fruit_rect = pygame.Rect(self.body ,cell_size, cell_size*2)
    def move_snake(self):
        body_copy = self.body[:-1]
        body_copy.insert(0,body_copy[0]+self.direction)
        self.body = body_copy[:]


class FRUIT:
    def __init__(self):
        self.x= random.randint(0,cell_number-1)
        self.y= random.randint(0,cell_number-1)
        self.pos = (Vector2(self.x*cell_size,self.y*cell_size))
    def draw_fruit(self):
        fruit_rect = pygame.Rect(self.pos.x,self.pos.y,cell_size,cell_size)
        pygame.draw.rect(screen,("red"),fruit_rect)

cell_size = 40
cell_number = 20

screen = pygame.display.set_mode((cell_size*cell_number, cell_size*cell_number))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()


pygame.display.flip()

running = True
fruit = FRUIT()
snake = SNAKE()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,150)

end=1
player_score = "0"

font = pygame.font.SysFont(None, 24)
img = font.render(player_score, True, "blue")

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
            fruit.pos=Vector2(random.randint(0,cell_number-1)*cell_size,random.randint(0,cell_number-1)*cell_size)
            snake.body.append(Vector2(fruit.pos/cell_size))
            print("ate an apple")
            end+=1
            player_score=str(int(player_score)+1)
            img = font.render(player_score, True, "blue")


        if snake.body[0][0]<0 or snake.body[0][0]>19 or snake.body[0][1]<0 or snake.body[0][1]>19:
            running=False

        for body in snake.body[3:]:

            if snake.body[0]==body:
                print(body, snake.body[0])
                running=False
                print("End!")




    screen.fill((255, 215, 70))
    screen.blit(img, (20, 20))
    fruit.draw_fruit()
    snake.draw_snake()


    #print([fruit.x,fruit.y])

    #logic end
    pygame.display.update()
    clock.tick(60)

pygame.quit()