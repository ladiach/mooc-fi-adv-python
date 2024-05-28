# WRITE YOUR SOLUTION HERE:
import pygame
from random import randint
    
pygame.init()
pygame.font.init()
pygame.display.set_caption("Asteroidit")
width, height = 640, 480
window = pygame.display.set_mode((width, height))
points = 0
    
class Asteroid:
    
    def __init__(self):
        self.image = pygame.image.load("rock.png")
        self.x = randint(0, width - self.image.get_width())
        self.y = randint(-2000, -1)
        self.height = self.image.get_height()
    
class Robot:
    
    def __init__(self):
        self.image = pygame.image.load("robot.png")
        self.x = randint(0,width- self.width())
        self.y = height - self.height()
    
    def width(self):
        return self.image.get_width()
    
    def height(self):
        return self.image.get_height()
    
    def movement(self, left = False, right = False):
        if left:
            self.x -= 2
        if right:
            self.x += 2
        if self.x <= 0:
            self.x = 0
        if self.x + self.width() >= width:
            self.x = width - self.width()
    
    
asteroids = [Asteroid() for i in range(15)]
    
robot = Robot()
    
clock = pygame.time.Clock()
    
    
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
    
    for i, asteroid in enumerate(asteroids):
        asteroid.y += 0.5
    
        if asteroid.y == height-asteroid.height:
            exit()
    
        collide_x = asteroid.x >= robot.x and asteroid.x <= robot.x+robot.width()
        collide_y = asteroid.y >= robot.y and asteroid.y <= robot.y + robot.height()
        if collide_x and collide_y:
            asteroids.pop(i)
            points += 1
    
    moves = pygame.key.get_pressed()
    if moves[pygame.K_LEFT]:
        robot.movement(left = True)
    if moves[pygame.K_RIGHT]:
        robot.movement(right = True)
    
    window.fill((0,0,0))
    
    window.blit(robot.image, (robot.x, robot.y))
    for asteroid in asteroids:
        window.blit(asteroid.image, (asteroid.x, asteroid.y))
    
    game_font = pygame.font.SysFont("Arial", 28)
    text = game_font.render(f"Points: {points}", True, (255,0,0))
    window.blit(text, (500,5))
    
    pygame.display.flip()
    
    clock.tick(60)