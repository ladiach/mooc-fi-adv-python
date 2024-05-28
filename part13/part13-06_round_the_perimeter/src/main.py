import pygame
    
pygame.init()
    
width, height = 640, 480
window = pygame.display.set_mode((width, height))
    
robot = pygame.image.load("robot.png")
h_robot = robot.get_height()
w_robot = robot.get_width()
    
x, y = 0, 0
velocity = 1
direction = 1
    
clock = pygame.time.Clock()
    
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
    window.fill((0,0,0))
    window.blit(robot, (x,y))
    pygame.display.flip()
    
    if direction == 1:
        x+=velocity
        if x + w_robot > width:
            direction = 2
    elif direction == 2:
        y+=velocity
        if y + h_robot > height:
            direction =3
    elif direction == 3:
        x -= velocity
        if x == 0:
            direction = 4
    elif direction == 4:
        y -= velocity
        if y == 0:
            direction = 1

    clock.tick(60)