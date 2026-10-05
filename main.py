import pygame # imma try make this in pygame
import sys

#setup
pygame.init()
screen = pygame.display.set_mode ((1200,800))
pygame.display.set_caption("Personality Test")
clock = pygame.time.Clock()

game_title = True
question_1 = False
running = True

title_font = pygame.font.SysFont("Impact", 150)
subtitle_font = pygame.font.SysFont("Impact", 80)
question_font = pygame.font.SysFont("Impact", 50)

#surfaces
title_surf = title_font.render("Personality Test", True, (255,255,255))
title_rect = title_surf.get_rect(center=(600,300))

message_surf = question_font.render("(press space to start)", True, (255,255,255))
message_rect = message_surf.get_rect(center=(600,550))

question_1_surf = subtitle_font.render("Q1. Whats your favorite color?", True, (255,255,255))
question_1_rect = question_1_surf.get_rect(center=(600,120))

question_1_1_surf = question_font.render("A. red", True, (255,255,255))
question_1_1_rect = question_1_1_surf.get_rect(center=(300,310))
question_1_2_surf = question_font.render("B. blue", True, (255,255,255))
question_1_2_rect = question_1_2_surf.get_rect(center=(900,310))
question_1_3_surf = question_font.render("C. green", True, (255,255,255))
question_1_3_rect = question_1_3_surf.get_rect(center=(300,590))
question_1_4_surf = question_font.render("D. yellow", True, (255,255,255))
question_1_4_rect = question_1_4_surf.get_rect(center=(900,590))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_title = False
                question_1 = True
   
    current_time = pygame.time.get_ticks()
    screen.fill((40,40,80))

    if game_title == True: # title screen
        screen.blit(title_surf, title_rect)
        if current_time >= 850:  # if the time is past 1 s and then half the time the message is on, half the time its not
            if current_time % 1700 < 850:
                screen.blit(message_surf, message_rect)
    elif question_1 == True:
        screen.fill((90,100,150))
        screen.blit(question_1_surf, question_1_rect)
        screen.blit(question_1_1_surf, question_1_1_rect)
        screen.blit(question_1_2_surf, question_1_2_rect)
        screen.blit(question_1_3_surf, question_1_3_rect)
        screen.blit(question_1_4_surf, question_1_4_rect)

    pygame.display.update()
    clock.tick(60)
pygame.quit()
sys.exit()
