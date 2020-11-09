import pygame

pygame.init()
size = (800, 600)
fps = 20 # Frames per second
screen = pygame.display.set_mode(size)

run=True
while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
