import pygame # imma try make this in pygame
import sys

pygame.init()
screen = pygame.display.set_mode ((1200,800))

running = True
while running:
    for event in pygame.event.get():
        if event.tpe == pygame.QUIT:
            running = False

    screen.fill((40,40,80))

    pygame.display.update()

pygame.quit()
sys.exit()