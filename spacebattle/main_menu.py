import pygame, sys
import tkinter

mainClock = pygame.time.Clock()

from pygame.locals import *

pygame.init()
pygame.display.set_caption("Space Battle")
icon = pygame.image.load('project.png')
pygame.display.set_icon(icon)

screen = pygame.display.set_mode((1080,800))

bg_menu = pygame.image.load('main1.jpg')
bg_menu = pygame.transform.scale(bg_menu, (1080, 800))

font_menu = pygame.font.SysFont('timesnewromanboldttf.ttf', 84)
font = pygame.font.SysFont('timesnewromanboldttf.ttf', 48)

print(pygame.font.get_fonts())
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

click = False

def main_menu():
    while True:
        screen.fill((0,0,0))
        screen.blit(bg_menu,(0,0))


        draw_text('Main Menu',font_menu , (255, 51, 255), screen, 400, 100)


        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(450, 250, 200, 50)
        button_2 = pygame.Rect(450, 350, 200, 50)
        button_3 = pygame.Rect(450, 450, 200, 50)
        button_4 = pygame.Rect(450, 550, 200, 50)

        if button_1.collidepoint((mx, my)):
            if click:
                game()
        if button_2.collidepoint((mx, my)):
            if click:
                settings()
        if button_3.collidepoint((mx, my)):
            if click:
                credits()
        if button_4.collidepoint((mx, my)):
            if click:
                pygame.quit()
                sys.exit()

        # t1 = font.render("Play" , True, (0, 0, 0))
        # t2 = font.render("Setting" , True, (0, 0, 0))
        # t3 = font.render("Exit" , True, (0, 0, 0))
        # screen.blit(t1, (450, 300))
        # screen.blit(t2, (450, 400))
        # screen.blit(t3, (450, 500))

        pygame.draw.rect(screen, (255, 178, 102), button_1)
        pygame.draw.rect(screen, (255, 178, 102), button_2)
        pygame.draw.rect(screen, (255, 178, 102), button_3)
        pygame.draw.rect(screen, (255, 178, 102), button_4)

        draw_text('Play', font, (0, 153, 0), screen, 515, 260)
        draw_text('Setting', font, (0, 0, 255), screen, 490, 360)
        draw_text('Credits', font, (0, 0, 255), screen, 490, 460)
        draw_text('Exit', font, (255, 0, 0), screen, 520, 560)
        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.type == K_SPACE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)

def game():
    running = True
    while running:
        screen.fill((0,0,0))

        draw_text('Game',font , (255,255,255), screen, 20, 20)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
        mainClock.tick(60)
def settings():
    running = True
    while running:
        screen.fill((0,0,0))

        draw_text('Settings',font , (255,255,255), screen, 20, 20)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
        mainClock.tick(60)
def credits():
    running = True
    while running:
        screen.fill((0, 0, 0))

        draw_text('Creators:',font_menu , (255, 255, 252), screen, 400, 100)

        draw_text('Nurdaulet', font, (0, 255, 255), screen, 455, 210)
        draw_text('Miras', font, (0, 255, 255), screen, 485, 310)
        draw_text('Sanzhar', font, (0, 255, 255), screen, 465, 410)
        draw_text('Bulat', font, (0, 255, 255), screen, 485, 510)
        draw_text('Amina', font, (0, 255, 255), screen, 475, 610)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
        mainClock.tick(60)

main_menu()