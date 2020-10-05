import pygame
import os.path
filepath = os.path.dirname(__file__)

pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Dungeon Crawler")


#Player
playerImage  = pygame.image.load(os.path.join(filepath, "assets/player2.png"))
playerX = 370
playerY = 480
playerX_change = 0
playerY_change = 0

enemyImage  = pygame.image.load(os.path.join(filepath, "assets/enemy.png"))
enemyX = 300
enemyY = 400


def player(x, y):
    screen.blit(playerImage, (x, y))

def enemy(x, y):
    screen.blit(enemyImage, (x, y))
#Game running
running = True
while running:
    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                playerX_change = -0.5
            if event.key == pygame.K_d:
                playerX_change =0.5
            if event.key == pygame.K_w:
                playerY_change = -0.5
            if event.key == pygame.K_s:
                playerY_change =0.5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                playerX_change = 0
            if event.key == pygame.K_w or event.key == pygame.K_s:
                playerY_change = 0
    
    
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >=760:
        playerX = 760

    playerY += playerY_change
    if playerY <= 0:
        playerY = 0
    elif playerY >=560:
        playerY = 560
        
    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()