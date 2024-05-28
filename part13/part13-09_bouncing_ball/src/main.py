# WRITE YOUR SOLUTION HERE:
import pygame
pygame.init()
    
width, height = 640, 480
window = pygame.display.set_mode((width, height))
    
ball = pygame.image.load("ball.png")
w_ball = ball.get_width()
h_ball = ball.get_height()
    
clock = pygame.time.Clock()
    
x, y = 300,200
x_velocity = 1
y_velocity = 1
    
    
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
    
    window.fill((0,0,0))
    window.blit(ball, (x,y))
    pygame.display.flip()
    
    x += x_velocity
    y += y_velocity
    
    if y + h_ball >= height or y<=0:
        y_velocity = -y_velocity
    
    if x + w_ball >= width or x<=0:
        x_velocity =-x_velocity
    
    clock.tick(60)