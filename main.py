import pygame
import random
pygame.init()
# colors
white=(255,255,255)
red=(255,0,0)
black=(0,0,0)
# creating window
height=600
width=800
food_x=random.randint(15,int(width/1.5))
food_y=random.randint(15,int(height/1.5))
gamewindow=pygame.display.set_mode((width,height))
pygame.display.set_caption('Snake Game')
pygame.display.update()
# game specific variable
exit_game=False
game_over=False
snake_x=width/2
snake_y=height/2
velocity_x=4
velocity_y=4
init_velocity=5
size=15
fps=30
score=0
clock=pygame.time.Clock()


# Game loop
while not exit_game:
    gamewindow.fill(white)
    pygame.draw.rect(gamewindow,black,[snake_x,snake_y,size,size])
    pygame.draw.rect(gamewindow, red, [food_x, food_y, size, size])
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit_game=True
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE:
                exit_game=True
            if event.key==pygame.K_RIGHT:
                velocity_x+=init_velocity
                velocity_y=0
            if event.key==pygame.K_LEFT:
                velocity_x-=init_velocity
                velocity_y=0
            if event.key==pygame.K_DOWN:
                velocity_y+=init_velocity
                velocity_x=0
            if event.key==pygame.K_UP:
                velocity_y-=init_velocity
                velocity_x=0
    snake_x+=velocity_x
    snake_y+=velocity_y
    if abs(snake_x-food_x)<7 and abs(snake_y-food_y)<7:
        score+=1
        print(score)
        food_x = random.randint(15, int(width/1.5))
        food_y = random.randint(15, int(height/1.5))






    clock.tick(fps)
pygame.quit()
quit()
