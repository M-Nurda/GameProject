import pygame

# Initialize the game
pygame.init()

# Frames per second
fps = 20

# Create the screen
screen = pygame.display.set_mode((800,600))

# Title and Icon
pygame.display.set_caption("Space Battle")
icon = pygame.image.load('project.png')
pygame.display.set_icon(icon)

run=True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill((0,255,255))
    pygame.display.update()