# WRITE YOUR SOLUTION HERE:
import pygame
from random import randint
    
pygame.init()
    
width, height = 640, 480
window = pygame.display.set_mode((width, height))
    
robot = pygame.image.load("robot.png")
window.fill((0,0,0))
    
for i in range(1000):
    x = randint(0,width-robot.get_width())
    y = randint(0,height-robot.get_height())
    window.blit(robot, (x, y))
    
pygame.display.flip()
    
    
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()