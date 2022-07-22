import pygame, sys, random
from pygame.locals import *

#--------------Global Variables-------------

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
clock = pygame.time.Clock()
running = True
bg_color = (0,0,0)
snake_color = (255, 0, 0)
snake_x, snake_y, snake_l, snake_w = 0, 0, 10, 10  
food_color = (0, 255, 0)
food_x, food_y, food_l, food_w = 100, 100 , 10, 10
food_pos = [food_x, food_y] 
score = 0
left = False        
right = False
up = False
down = False
vel = 4     
level = 10            #vel of the snake
history = [None, None]
snake_body = [[snake_x, snake_y]]

#----------------Screen---------------------

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('Snake')

#---------------Functions-------------------

def move(direction, vel):
    global snake_x, snake_y
    if direction == 'left':
        snake_x -= vel
    if direction == 'right':
        snake_x += vel
    if direction == 'up':
        snake_y -= vel
    if direction == 'down':
        snake_y += vel

def collision(snake, food):
    if snake.colliderect(food):
        return True
    return False

def food_generator(food_pos):
    food_x = random.randint(0, SCREEN_WIDTH - 10)
    food_y = random.randint(0, SCREEN_HEIGHT - 10)
    return food_x, food_y

#--------------Main Loop--------------------

while running:   
    screen.fill(bg_color)
    snake = pygame.Rect(snake_x, snake_y, snake_l, snake_w)
    food = pygame.Rect(food_pos[0], food_pos[1], food_l, food_w)
    pygame.draw.rect(screen, snake_color, snake)
    pygame.draw.rect(screen, food_color, food)
    pygame.time.delay(level)
      
    #Border Collision Check
    if snake_x >= SCREEN_WIDTH-snake_l or snake_x < 0 or snake_y >= SCREEN_HEIGHT-snake_w or snake_y < 0:
        running = False

    if left:
        if history[0] == 'right':
            move('right',vel)
            history[1] = 'right'
        else:
            move('left', vel)
        if collision(snake, food):
            food_pos[0], food_pos[1] = food_generator(food_pos)
    if right:
        if history[0] == 'left':
            move('left',vel)
            history[1] = 'left'
        else:
            move('right', vel)
        if collision(snake, food):
            food_pos[0], food_pos[1] = food_generator(food_pos)
    if up:
        if history[0] == 'down':
            move('down',vel)
            history[1] = 'down'
        else:
            move('up', vel)
        if collision(snake, food):
            food_pos[0], food_pos[1] = food_generator(food_pos)
    if down:
        if history[0] == 'up':
            move('up',vel)
            history[1] = 'up'
        else:
            move('down', vel)
        if collision(snake, food):
            food_pos[0], food_pos[1] = food_generator(food_pos)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                left = True
                history[0] = history[1]
                history[1] = 'left'
                right, up, down = False, False, False
            if event.key == K_RIGHT:
                right = True
                history[0] = history[1]
                history[1] = 'right'
                left, up, down = False, False, False
            if event.key == K_UP:
                up = True
                history[0] = history[1]
                history[1] = 'up'
                left, right, down = False, False, False
            if event.key == K_DOWN:
                down = True
                history[0] = history[1]
                history[1] = 'down'
                left, right, up = False, False, False
    pygame.display.update()
    clock.tick(60)
