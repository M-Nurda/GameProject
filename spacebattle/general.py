import pygame
import random
# Initialize the game
pygame.init()

# Frames per second
fps = 20

# Create the screen
screen = pygame.display.set_mode((1080,800))

# Title and Icon
pygame.display.set_caption("Space Battle")
icon = pygame.image.load('project.png')
pygame.display.set_icon(icon)


# Player 1
# Load spaceship picture
playerImg = pygame.image.load('spaceship.png')
# Change the size of spaceship
playerImg = pygame.transform.scale(playerImg, (60, 60))
# Initial Position of spaceship
playerX = 520
playerY = 700
playerX_change = 0

# Enemy
# Load enemy picture
enemyImg = pygame.image.load('ufo.png')
# Change the size of enemy
enemyImg = pygame.transform.scale(enemyImg, (60, 60))
# Initial Position of enemy
enemyX = random.randint(200,680)
enemyY = random.randint(50, 100)
enemyX_change = 0.3
enemyY_change = 10

def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(x, y):
    screen.blit(enemyImg, (x, y))

run=True
while run:
    #RGB = Red, Green, Blue -> background color
    screen.fill((0,0,0))
    a = random.randint(210, 260)
    b = random.randint(750, 800)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if event.type == pygame.KEYDOWN:
        print("Keyboard pressed")
        if event.key == pygame.K_LEFT:
            playerX_change = -1
        if event.key == pygame.K_RIGHT:
            playerX_change = 1
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            playerX_change = 0

    # Boundries Check
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 1020:
        playerX = 1020

    # Enemy movement
    enemyX += enemyX_change
    if enemyX <= a:
        enemyX_change = 0.3
        enemyY += enemyY_change
    elif enemyX >= b:
        enemyX_change = -0.3
        enemyY += enemyY_change


    player(playerX, playerY)
    enemy(enemyX, enemyY)

    pygame.display.update()