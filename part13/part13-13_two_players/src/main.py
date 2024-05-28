# WRITE YOUR SOLUTION HERE:
class Player:
    
    def __init__(self):
        self.image = pygame.image.load("robot.png")
        self.x = 0
        self.y = 0
        self.right = False
        self.left = False
        self.down = False
        self.up = False
    
    
import pygame
pygame.init()
    
width, height = 640, 480
window = pygame.display.set_mode((width, height))
    
velocity = 10
    
player1 = Player()
player2 = Player()
    
player1.x, player1.y = 100,100
player2.x, player2.y = 300,300
clock = pygame.time.Clock()
    
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player1.up = True
            if event.key == pygame.K_a:
                player1.left = True
            if event.key == pygame.K_s:
                player1.down = True
            if event.key == pygame.K_d:
                player1.right = True
            if event.key == pygame.K_UP:
                player2.up = True
            if event.key == pygame.K_LEFT:
                player2.left = True
            if event.key == pygame.K_DOWN:
                player2.down = True
            if event.key == pygame.K_RIGHT:
                player2.right = True
    
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                player1.up = False
            if event.key == pygame.K_a:
                player1.left = False
            if event.key == pygame.K_s:
                player1.down = False
            if event.key == pygame.K_d:
                player1.right = False
            if event.key == pygame.K_UP:
                player2.up = False
            if event.key == pygame.K_LEFT:
                player2.left = False
            if event.key == pygame.K_DOWN:
                player2.down = False
            if event.key == pygame.K_RIGHT:
                player2.right = False
    
    
    
    
    if player1.up:
        player1.y -= velocity
    if player1.left:
        player1.x -= velocity
    if player1.down:
        player1.y += velocity
    if player1.right:
        player1.x += velocity
    
    if player2.up:
        player2.y -= velocity
    if player2.left:
        player2.x -= velocity
    if player2.down:
        player2.y += velocity
    if player2.right:
        player2.x += velocity
    
    player1.y = max(0,player1.y) #doesn't go above the top
    player1.x = max(0, player1.x) #within the left wall
    player1.y = min(player1.y, height-player1.image.get_height()) #above the bottom wall
    player1.x = min(player1.x, width - player1.image.get_width()) #within the right wall
    
    player2.y = max(0, player2.y)
    player2.x = max(0, player2.x)
    player2.y = min(player2.y, height-player2.image.get_height())
    player2.x = min(player2.x, width - player2.image.get_width())
    
    
    
    
    window.fill((0,0,0))
    window.blit(player1.image, (player1.x,player1.y))
    window.blit(player2.image, (player2.x, player2.y))
    pygame.display.flip()
    
    clock.tick(60)