# WRITE YOUR SOLUTION HERE:
import pygame
pygame.init()
    
width, height = 640, 480
window = pygame.display.set_mode((width, height))
    
robot = pygame.image.load("robot.png")
    
x = width/2 - robot.get_width()/2
y = height/2 - robot.get_height()/2
    
to_right = False
to_left = False
to_up = False
to_down = False
    
velocity = 5
    
clock = pygame.time.Clock()
    
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                to_right = True
            if event.key == pygame.K_LEFT:
                to_left = True
            if event.key == pygame.K_UP:
                to_up = True
            if event.key == pygame.K_DOWN:
                to_down = True
    
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                to_right = False
            if event.key == pygame.K_LEFT:
                to_left = False
            if event.key == pygame.K_UP:
                to_up = False
            if event.key == pygame.K_DOWN:
                to_down = False
    
    if x + robot.get_width()> width:
        to_right = False
    if x == 0:
        to_left = False
    if y + robot.get_height() > height:
        to_down = False
    if y <= 0:
        to_up = False
    
    if to_right:
        x += velocity
    if to_left:
        x -= velocity
    if to_down:
        y += velocity
    if to_up:
        y -= velocity
    
    
    
    window.fill((0,0,0))
    window.blit(robot, (x,y))
    pygame.display.flip()
    
    clock.tick(60)