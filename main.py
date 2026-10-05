import pygame # imma try make this in pygame
import sys

#setup
pygame.init()
screen = pygame.display.set_mode ((1200,800))
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((40,40,80))

    pygame.display.update()
    clock.tick(60)
pygame.quit()
sys.exit()