import pygame, sys, random
from pygame.locals import *


#--------------Global Variables-------------

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
clock = pygame.time.Clock()
running = True
bg_color = (0,0,0)
snake_color = (255, 255, 255)
snake_x, snake_y, snake_l, snake_w = 0, 0, 20, 20  
food_color = (200, 0, 0)
food_x, food_y, food_l, food_w = 100, 100 , 10, 10
food_pos = [food_x, food_y]
score = 0
left = False        
right = False
up = False
down = False
vel = 4                 #vel of the snake
history = [None, None]  #Tracks movement history



#----------------Screen---------------------

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('Snake')


#---------------Functions-------------------

def move(history, vel):
    global snake_x, snake_y

    #Stopping Backwards Movement
    if history[0] != history[1]:
        if history[1] == 'left' and history[0] != 'right':
            snake_x -= vel
        if history[1] == 'left' and history[0] == 'right':
            snake_x += vel
        if history[1] == 'right' and history[0] != 'left':
            snake_x += vel
        if history[1] == 'right' and history[0] == 'left':
            snake_x -= vel
        if history[1] == 'up' and history[0] != 'down':
            snake_y -= vel
        if history[1] == 'up' and history[0] == 'down':
            snake_y += vel
        if history[1] == 'down' and history[0] != 'up':
            snake_y += vel
        if history[1] == 'down' and history[0] == 'up':
            snake_y -= vel


    # if movement == 'left':
    #     snake_x -= vel
    # if movement == 'right':
    #     snake_x += vel
    # if movement == 'up':
    #     snake_y -= vel
    # if movement == 'down':
    #     snake_y += vel

def collision(snake, food):
    if snake.colliderect(food):
        return True
    return False

def food_generator(food_pos):
    food_x = random.randint(0, SCREEN_WIDTH)
    food_y = random.randint(0, SCREEN_HEIGHT)
    return food_x, food_y


#--------------Main Loop--------------------

while running:
    
    screen.fill(bg_color)
    snake = pygame.Rect(snake_x, snake_y, snake_l, snake_w)
    food = pygame.Rect(food_pos[0], food_pos[1], food_l, food_w)
    pygame.draw.rect(screen, snake_color, snake)
    pygame.draw.rect(screen, food_color, food)
   
    #Border Collision Check
    if snake_x >= SCREEN_WIDTH-snake_l or snake_x < 0 or snake_y >= SCREEN_HEIGHT-snake_w or snake_y < 0:
        running = False

    if left:
        move(history, vel) 
        if collision(snake, food):
            snake_l += 5       
            score += 1
            food_pos[0], food_pos[1] = food_generator(food_pos)

    if right:
        move(history, vel)
        if collision(snake, food):
            snake_l += 5       
            score += 1
            food_pos[0], food_pos[1] = food_generator(food_pos)
    if up:
        move(history, vel) 
        if collision(snake, food):
            snake_l += 5       
            score += 1
            food_pos[0], food_pos[1] = food_generator(food_pos)
    if down:
        move(history,  vel) 
        if collision(snake, food):
            snake_l += 5      
            score += 1
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
