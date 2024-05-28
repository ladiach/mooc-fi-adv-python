# WRITE YOUR SOLUTION HERE:
import pygame
    
pygame.init()
    
width, height = 640, 480
window = pygame.display.set_mode((width, height))
    
robot = pygame.image.load("robot.png")
w_robot = robot.get_width()
    
robot_two = pygame.image.load("robot.png")
w_robot_two = robot.get_width()
    
x, y = 0,40
velocity = 1
    
x_two, y_two = 0, 150
velocity_two = velocity *2
    
clock = pygame.time.Clock()
    
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
    window.fill((0,0,0))
    window.blit(robot, (x,y))
    window.blit(robot_two, (x_two, y_two))
    pygame.display.flip()
    
    x += velocity
    x_two += velocity_two
    
    if velocity >0 and x + w_robot > width:
        velocity = -velocity
    
    if velocity < 0 and x <= 0:
        velocity = -velocity
    
    
    if velocity_two > 0 and x_two + w_robot_two > width:
        velocity_two = -velocity_two
    
    if velocity_two < 0 and x_two <= 0:
        velocity_two = -velocity_two
    clock.tick(60)