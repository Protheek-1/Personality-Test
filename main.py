import pygame # imma try make this in pygame
import sys

#setup
pygame.init()
screen = pygame.display.set_mode ((1200,800))
clock = pygame.time.Clock()

title_font = pygame.font.SysFont("Impact", 150)
question_font = pygame.font.SysFont("Impact", 50)


title_surf = title_font.render("Personality Test", True, (255,255,255))
title_rect = title_surf.get_rect(center=(600,300))

message_surf = question_font.render("(press space to start)", True, (255,255,255))
message_rect = message_surf.get_rect(center=(600,550))

game_title = True

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
   
    current_time = pygame.time.get_ticks()
    screen.fill((40,40,80))

    if game_title == True:
        screen.blit(title_surf, title_rect)
        if current_time >= 1000:
            if current_time % 1700 < 850:
                screen.blit(message_surf, message_rect)
    

    pygame.display.update()
    clock.tick(60)
pygame.quit()
sys.exit()
