# WRITE YOUR SOLUTION HERE:
from random import randint
import pygame
pygame.init()
    
class Robot:
    
    def __init__(self):
        self.image = pygame.image.load("robot.png")
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.x = randint(0,width)
        self.y = randint(-500,0)
        self.__direction = randint(1,2)
    
    @property
    def direction(self):
        return self.__direction
    
    
    def x_right(self):
        self.x += x_velocity
        self.y = height - self.height
    
    def x_left(self):
        self.x -= x_velocity
        self.y = height - self.height
    
    
    
    
width, height = 640, 480
window = pygame.display.set_mode((width, height))
    
clock = pygame.time.Clock()
    
    
y_velocity = 1
x_velocity = 1
    
robots = [Robot() for i in range(10)]
    
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
    window.fill((0,0,0))
    for robot in robots:
        window.blit(robot.image, (robot.x,robot.y))
    
    for i, robot in enumerate(robots):
        robot.y += y_velocity
    
        if robot.y+robot.height >height:
            if robot.direction == 1:
                robot.x_right()
            if robot.direction == 2:
                robot.x_left()
    
        if robot.x+robot.width> width or robot.x ==0:
            robots.pop(i)
    
    pygame.display.flip()
    
    clock.tick(60)