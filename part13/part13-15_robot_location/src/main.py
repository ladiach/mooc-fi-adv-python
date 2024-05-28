# WRITE YOUR SOLUTION HERE:
from random import randint
import pygame
pygame.init()
    
width, height = 640, 480
window = pygame.display.set_mode((width, height))
    
robot = pygame.image.load("robot.png")
w_robot = robot.get_width()
h_robot = robot.get_height()
r_rect = robot.get_rect()
    
r_rect.x = randint(0, width-w_robot)
r_rect.y = randint(0, height-h_robot)
    
    
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_x, mouse_y = pygame.mouse.get_pos() #get click position
            #print(f'Mouse clicked at {mouse_x}, {mouse_y}')
            if r_rect.collidepoint((mouse_x,mouse_y)):
                r_rect.x = randint(0, width - w_robot)
                r_rect.y = randint(0, height - h_robot)
    
    window.fill((0,0,0))
    window.blit(robot, r_rect)
    pygame.display.flip()