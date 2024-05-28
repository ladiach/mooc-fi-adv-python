# WRITE YOUR SOLUTION HERE:
import pygame
pygame.init()
    
width = 640
height = 480
window = pygame.display.set_mode((width, height))
    
robot = pygame.image.load("robot.png")
window.fill((0,0,0))
    
for i in range(10):    
    for j in range(10):
        window.blit(robot, (50+15*i+40*j, 100+20*i))
    
    
pygame.display.flip()
    
    
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()