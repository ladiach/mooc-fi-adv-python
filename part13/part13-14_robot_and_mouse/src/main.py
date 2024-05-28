# WRITE YOUR SOLUTION HERE:
import pygame
pygame.init()
    
width, height = 640, 480
window = pygame.display.set_mode((width, height))
    
robot = pygame.image.load("robot.png")
w_robot = robot.get_width()
h_robot = robot.get_height()
    
x, y = 200,100
    
clock = pygame.time.Clock()
    
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        
        if event.type == pygame.MOUSEMOTION:
            x = event.pos[0]-w_robot/2
            y = event.pos[1]-h_robot/2
    
    
    window.fill((0,0,0))
    window.blit(robot, (x,y))
    pygame.display.flip()
    
    clock.tick(60)