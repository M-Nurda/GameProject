import pygame
import random
import math
from pygame import mixer
# Initialize the game
pygame.init()

# Frames per second
fps = 60

# Create the screen
screen = pygame.display.set_mode((1080,800))

# Background
bg = pygame.image.load('bg4.jpeg')
bg = pygame.transform.scale(bg, (1080, 800))

# Background sound
mixer.music.load('bg3_music.wav')
mixer.music.play(-1)

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
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []

enemyNum = 6
for i in range(enemyNum):
    # Load enemy picture
    temp=pygame.image.load('ufo.png')
    # Change the size of enemy
    temp = pygame.transform.scale(temp, (60, 60))
    # enemyImg.append(pygame.image.load('ufo.png'))
    enemyImg.append(temp)

    # Initial Position and Speed of enemy
    enemyX.append(random.randint(200,799))
    enemyY.append(random.randint(30, 70))
    enemyX_change.append(0.3)
    enemyY_change.append(10)

# Right Ammo
# Load ammo picture
ammoImg2 = pygame.image.load('ammo.png')
# Change the size of enemy
ammoImg2 = pygame.transform.scale(ammoImg2, (30, 45))
# Initial Position and Speed of enemy
ammoX2 = 0
ammoY2 = 700
ammoX_change2 = 0
ammoY_change2 = 2
ammo_state2 = "ready"

# Left Ammo
# Load ammo picture
ammoImg1 = pygame.image.load('ammo.png')
# Change the size of enemy
ammoImg1 = pygame.transform.scale(ammoImg1, (30, 45))
# Initial Position and Speed of enemy
ammoX1 = 0
ammoY1 = 700
ammoX_change1 = 0
ammoY_change1 = 2
ammo_state1 = "ready"

# Points
points = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 900
textY = 20

def show_points(x, y):
    score = font.render("Score: " + str(points), True, (0,255,0))
    screen.blit(score, (x, y))

def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))

def fire_ammo2(x, y):
    global ammo_state2
    ammo_state2 = 'fired'
    screen.blit(ammoImg2, (x + 41, y - 25))

def fire_ammo1(x, y):
    global ammo_state1
    ammo_state1 = 'fired'
    screen.blit(ammoImg2, (x - 12, y - 25))

def isCollision(enemyX,enemyY,ammoX1,ammoY1,ammoX2,ammoY2):
    dist1 = math.sqrt((enemyX-ammoX1)**2+(enemyY-ammoY1)**2)
    dist2 = math.sqrt((enemyX-ammoX2)**2+(enemyY-ammoY2)**2)
    if dist1 < 27 or dist2 < 27:
        return True
    else:
        return False

run=True
while run:
    # RGB = Red, Green, Blue -> background color
    screen.fill((0,0,0))

    # Background
    screen.blit(bg,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            playerX_change = -2
        if event.key == pygame.K_RIGHT:
            playerX_change = 2
        if event.key == pygame.K_UP:
            if ammo_state1 == 'ready' and ammo_state2 == 'ready':
                shot_sound = mixer.Sound('pew.wav')
                shot_sound.play()

                ammoX1 = playerX
                ammoX2 = playerX
                fire_ammo2(playerX, ammoY2)
                fire_ammo1(playerX, ammoY1)

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            playerX_change = 0

    # Boundries Check
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 1020:
        playerX = 1020

    # Enemy movement direction and speed change
    for i in range(enemyNum):
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 200:
            enemyX_change[i] = 0.3
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 800:
            enemyX_change[i] = -0.3
            enemyY[i] += enemyY_change[i]

        # Collision laser and enemy
        collision = isCollision(enemyX[i], enemyY[i], ammoX1, ammoY1, ammoX2, ammoY2)
        if collision:
            boom_sound = mixer.Sound('boom.wav')
            boom_sound.play()


            ammoY1 = 700
            ammoY2 = 700
            ammo_state2 = 'ready'
            ammo_state1 = 'ready'
            points += 10
            enemyX[i] = random.randint(200, 799)
            enemyY[i] = random.randint(50, 100)

        enemy(enemyX[i],enemyY[i],i)

    if ammoY1 <= 0 and ammoY2 <= 0:
        ammoY1 = 700
        ammoY2 = 700
        ammo_state1 = 'ready'
        ammo_state2 = 'ready'

    # Laser2 movement
    if ammo_state2 == 'fired' and ammo_state1 == 'fired':
        fire_ammo2(ammoX2, ammoY2)
        fire_ammo1(ammoX1, ammoY1)
        ammoY2 -= ammoY_change2
        ammoY1 -= ammoY_change1




    player(playerX, playerY)
    # enemy(enemyX, enemyY)
    show_points(textX, textY)
    pygame.display.update()