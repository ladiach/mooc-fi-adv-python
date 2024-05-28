# WRITE YOUR SOLUTION HERE:
import pygame
import datetime
import math
    
pygame.init()
    
width, height = 640, 480
window = pygame.display.set_mode((width, height))
center = width/2, height/2
    
clock = pygame.time.Clock()
    
radius = 200

def draw_hand(length:int, thickness:int, proportion:float):
    angle = 2*math.pi*proportion-math.pi/2
    end_x = center_x+math.cos(angle)*length
    end_y = center_y+math.sin(angle)*length

    pygame.draw.line(window, (0,0,255), (center_x, center_y), (end_x,end_y),thickness)
    
    
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
    window.fill((0,0,0))
    
    time = datetime.datetime.now()
    time_formatted = time.strftime("%H:%M:%S")
    pygame.display.set_caption(time_formatted)
    
    hours, minutes, seconds = time.hour % 12, time.minute, time.second

    center_x = width/2
    center_y = height/2
    
    #seconds
    draw_hand(185, 1, seconds/60)
    
    #minute
    draw_hand(170,4,(minutes+seconds/60)/60)
    
    #hour
    draw_hand(150,7, (hours+minutes/60+seconds/3600)/12)

    
    #order of circle attributes: surface, colour, origin, radius, width
    pygame.draw.circle(window, (255, 0,0), center, radius, 5)
    pygame.draw.circle(window, (255,0,0), center,10)
    
    
    pygame.display.flip()