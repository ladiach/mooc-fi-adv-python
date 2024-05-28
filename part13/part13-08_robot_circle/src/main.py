# WRITE YOUR SOLUTION HERE:
import pygame
import math
    
pygame.init()
    
width, height = 640, 480
window = pygame.display.set_mode((width, height))
    
robot = pygame.image.load("robot.png")
    
angle = 0
    
clock = pygame.time.Clock()
    
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
    radius = 100
    robots = 10
    
    
    window.fill((0,0,0))
    
    
    for i in range(robots):
        x = 320+math.cos(angle+2*math.pi*i/robots)*radius-robot.get_width()/2
        y = 240+math.sin(angle+2*math.pi*i/robots)*radius-robot.get_height()/2
        window.blit(robot, (x, y))
    
    pygame.display.flip()
    
    angle += 0.01
    
    clock.tick(60)