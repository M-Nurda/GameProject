import pygame, sys
import random
import math
from pygame import mixer
# Initialize the game
pygame.init()

# Frames per second
fps = 144

# Create the screen
screen = pygame.display.set_mode((1080,800))
# Clock
clock = pygame.time.Clock()
# Background
bg = pygame.image.load('bg4.jpeg')
bg = pygame.transform.scale(bg, (1080, 800))

# Background sound
# mixer.music.load('bg3_music.wav')
# mixer.music.play(-1)

# Title and Icon
pygame.display.set_caption("Space Battle")
icon = pygame.image.load('project.png')
pygame.display.set_icon(icon)

#Fonts
menu_font = pygame.font.Font('freesansbold.ttf', 32)


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
    temp = pygame.image.load('ufo.png')
    # Change the size of enemy
    temp = pygame.transform.scale(temp, (60, 60))
    # enemyImg.append(pygame.image.load('ufo.png'))
    enemyImg.append(temp)

    # Initial Position and Speed of enemy
    enemyX.append(random.randint(200,799))
    enemyY.append(random.randint(30, 70))
    enemyX_change.append(1)
    enemyY_change.append(50)

# Meteor
meteorImg = []
meteorX = []
meteorY = []
mX_change = []
mY_change = []
for i in range(15):
    copy = pygame.image.load('asteroid.png')
    copy = pygame.transform.scale(copy, (random.randint(40,60), random.randint(40,70)))
    meteorImg.append(copy)
    # Initial Position and Speed of enemy
    meteorX.append(random.randint(0,150))
    meteorY.append(random.randint(5,8))
    mY_change.append(random.uniform(1, 3))
    mX_change.append(0)

meteorImg1 = []
meteorX1 = []
meteorY1 = []
mX_change1 = []
mY_change1 = []
for i in range(15):
    copy1 = pygame.image.load('asteroid.png')
    copy1 = pygame.transform.scale(copy1, (random.randint(40,60), random.randint(40,70)))
    meteorImg.append(copy1)
    # Initial Position and Speed of enemy
    meteorX1.append(random.randint(820,1050))
    meteorY1.append(random.randint(3,8))
    mY_change1.append(random.uniform(1, 6))
    mX_change1.append(0)


# Right Ammo
# Load ammo picture
ammoImg2 = pygame.image.load('ammo.png')
# Change the size of enemy
ammoImg2 = pygame.transform.scale(ammoImg2, (30, 45))
# Initial Position and Speed of enemy
ammoX2 = 0
ammoY2 = 700
ammoX_change2 = 0
ammoY_change2 = 5
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
ammoY_change1 = 5
ammo_state1 = "ready"

# Points
points = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 900
textY = 10
# Level
levelX = 420
levelY = 10

#Game Over Text
gg_font=pygame.font.Font('freesansbold.ttf', 32)

# Health point
black_bar = pygame.Surface((1080, 45))

# def show_level(x, y):
#     if points < 100:
#         # x='Level 1 - Easy'
#         level = font.render('Level 1 - Easy', True, (255, 0, 0))
#     elif points >= 100:
#         # x='Level 2 - Medium'
#         level = font.render('Level 2 - Medium', True, (255, 0, 0))
#     elif points >= 200:
#         # x='Level 3 - Hard'
#         level = font.render('Level 3 - Hard', True, (255, 0, 0))
#     elif points >= 300:
#         # x='Level 4 - Well Played'
#         level = font.render('Level 4 - Super Hard', True, (255, 0, 0))
#     elif points >= 400:
#         # x='Level 5 - You nut'
#         level = font.render('Level 5 - You nut', True, (255, 0, 0))
#
#     # level = font.render('Level', True, (255, 0, 0))
#     screen.blit(level, (x, y))

# def show_points(x, y):
#     score = font.render("Score: " + str(points), True, (0,255,0))
#     screen.blit(score, (x, y))

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def bb(black_bar, x, y):
    screen.blit(black_bar, (x, y))
    pygame.draw.rect(screen, (95,95,95), (0, 0, 1080, 45), 3)

def hp(surface, player_shield):
    if player_shield > 150:
        player_shield_color = (0,252,134)
        player_shield = 100
    elif player_shield > 130:
        player_shield_color = (0,252,52)
    elif player_shield > 110:
        player_shield_color = (117,252,0)
    elif player_shield > 90:
        player_shield_color = (252,252,0)
    elif player_shield > 70:
        player_shield_color = (252,218,0)
    elif player_shield > 50:
        player_shield_color = (252,159,51)
    elif player_shield > 30:
        player_shield_color = (255,84,51)
    else:
        player_shield_color= (255,0,0)

    pygame.draw.rect(surface, (95, 95, 95), (5, 5, 155, 34), 3)
    pygame.draw.rect(surface, player_shield_color, (7, 7, player_shield, 30))

def GG():
    gg_text = font.render("GAME OVER", True, (255,0,0))
    score_t = font.render("Score: "+ str(points), True, (255,255,0))

    screen.blit(gg_text, (450, 300))
    screen.blit(score_t, (450, 350))

def set_difficulty(value, difficulty):
    pass

def player(x, y):
    screen.blit(playerImg, (x, y))

def meteor(x, y, i):
    screen.blit(meteorImg[i], (x, y))

def meteor1(x, y, i):
    screen.blit(meteorImg1[i], (x, y))

def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))

def fire_ammo2(x, y):
    global ammo_state2
    ammo_state2 = 'fired'
    screen.blit(ammoImg2, (x + 41, y - 25))

def fire_ammo1(x, y):
    global ammo_state1
    ammo_state1 = 'fired'
    screen.blit(ammoImg1, (x - 12, y - 25))

def isCollision(enemyX,enemyY,ammoX1,ammoY1,ammoX2,ammoY2):
    dist1 = math.sqrt((enemyX-ammoX1)**2+(enemyY-ammoY1)**2)
    dist2 = math.sqrt((enemyX-ammoX2)**2+(enemyY-ammoY2)**2)

    if dist1 < 27 or dist2 < 27:
        # print(dist1, dist2)
        return True
    else:
        return False

def touched1(enemyX,enemyY,playerX, playerY):
    dist1 = math.sqrt((enemyX-playerX)**2+(enemyY-playerY)**2)
    if dist1 < 27:
        print(dist1)
        return True
    else:
        return False
def touched2(enemyX,enemyY,playerX, playerY):
    dist1 = math.sqrt((enemyX-playerX)**2+(enemyY-playerY)**2)
    if dist1 < 27:
        print(dist1)
        return True
    else:
        return False

global c
hp_bar=0
while True:
    c=0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # RGB = Red, Green, Blue -> background color
    screen.fill((0,0,0))

    # Background menu
    screen.blit(bg,(0,0))
    # screen.blit(bg_menu,(0,0))


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
        #Game over
        if enemyY[i]>700 and hp_bar<150:
            for j in range(enemyNum):
                enemyY[j]=random.randint(10,30)
                # c += 1
                hp_bar+=random.randint(5,10)
            # GG()
        elif hp_bar>=150:
            for j in range(enemyNum):
                enemyY[j] = 2000
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 200:
            if points < 100:
                enemyX_change[i] = 1
            elif points >= 100:
                enemyX_change[i] = 3
            elif points >= 200:
                enemyX_change[i] = 5
            elif points >= 300:
                enemyX_change[i] = 7
            elif points >= 400:
                enemyX_change[i] = 10
            enemyY[i] += enemyY_change[i]

        elif enemyX[i] >= 800:
            if points < 100:
                enemyX_change[i] = -1
            elif points >= 100:
                enemyX_change[i] = -3
            elif points >= 200:
                enemyX_change[i] = -5
            elif points >= 300:
                enemyX_change[i] = -7
            elif points >= 400:
                enemyX_change[i] = -10
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
            enemyY[i] = 50
        enemy(enemyX[i],enemyY[i],i)

    # Meteor left
    for i in range(15):
        # if c>0:
        #     for j in range(15):
        #         meteorX[j]=2000
        #     break
        # else:
        touch1 = touched1(meteorX[i], meteorY[i], playerX, playerY)
        if touch1==True:
            boom_sound = mixer.Sound('boom.wav')
            boom_sound.play()
            for j in range(15):
                meteorX[j]=2000
                c+=1
            break

        meteorY[i] += mY_change[i]
        if meteorY[i] >= 800:
            mY_change[i] = random.uniform(1, 4)
            meteorY[i] = 0
            # meteorX[i] = random.randint(c+0, c+150)
            meteorY[i] += mY_change[i]
        meteor(meteorX[i], meteorY[i], i)

    # Meteor Right
    for i in range(15):
        # if c>0:
        #     for j in range(15):
        #         meteorX1[j]=2000
        #     break
        # else:
        touch2 = touched1(meteorX1[i], meteorY1[i], playerX, playerY)
        if touch2==True:
            boom_sound = mixer.Sound('boom.wav')
            boom_sound.play()
            for j in range(15):
                meteorX1[j]=2000
                c+=1
            break

        meteorY1[i] += mY_change1[i]
        if meteorY1[i] >= 800:
            mY_change1[i] = random.uniform(1, 4)
            meteorY1[i] = 0
            # meteorX[i] = random.randint(c+0, c+150)
            meteorY1[i] += mY_change1[i]
        meteor(meteorX1[i], meteorY[i], i)


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

    if c>0 or hp_bar>=150:
        for i in range(enemyNum):
            enemyY[i] = 2000
        for i in range(15):
            meteorX[i] = 2000
            meteorX1[i] = 2000
        playerY = 2000
        hp(screen, 0)
        hp_bar=150
        GG()
    player(playerX, playerY)
    bb(black_bar, 0, 0)

    draw_text('Score: ' + str(points), font, (0, 255, 0), screen, textX, textY)
    if points < 100:
        level = 'Level 1 - Easy'
    elif points >= 100:
        if points == 100:
            level_up = 1
            if level_up == 1:
                up = mixer.Sound('levelup.wav')
                up.play()
        level = 'Level 2 - Medium'
    elif points >= 200:
        if points == 200:
            level_up = 2
            if level_up == 2:
                up = mixer.Sound('levelup.wav')
                up.play()
        level = 'Level 3 - Hard'
    elif points >= 300:
        if points == 300:
            level_up = 3
            if level_up == 3:
                up = mixer.Sound('levelup.wav')
                up.play()
        level = 'Level 4 - Super Hard'
    elif points >= 400:
        if points == 400:
            level_up = 4
            if level_up == 4:
                up = mixer.Sound('levelup.wav')
                up.play()
        level = 'Level 5 - You nut'
    draw_text(level, font, (255, 0, 0), screen, levelX, levelY)
    hp(screen, 150-hp_bar)
    print(150, 150-hp_bar, hp_bar)
    pygame.display.update()
    clock.tick(fps)


