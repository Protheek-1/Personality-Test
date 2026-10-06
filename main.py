import pygame # imma try make this in pygame
import sys
import math

#setup
pygame.init()
screen = pygame.display.set_mode ((1200,800))
pygame.display.set_caption("Personality Test")
clock = pygame.time.Clock()


game_title = "TITLE"
running = True


title_font = pygame.font.Font('fonts/gorditas.ttf', 120)
subtitle_font = pygame.font.Font('fonts/gorditas.ttf', 80)
question_font = pygame.font.Font('fonts/gorditas.ttf', 50)

#surfaces
title_surf = title_font.render("Personality Test", True, (255,255,255))
title_rect = title_surf.get_rect(center=(600,300))

message_surf = question_font.render("(press space to start)", True, (255,255,255))
message_rect = message_surf.get_rect(center=(600,550))

#title page bg
tri_width = 140
tri_height = int(tri_width * (math.sqrt(3)/2))
corner_radius = 16
gap = 80
tri_colour = (250, 160, 170)

triangle_surf = pygame.Surface((tri_width, tri_height), pygame.SRCALPHA)
p1 = (tri_width // 2, corner_radius)
p2 = (corner_radius, tri_height - corner_radius)
p3 = (tri_width - corner_radius, tri_height - corner_radius)

pygame.draw.circle(triangle_surf, tri_colour, p1, corner_radius)
pygame.draw.circle(triangle_surf, tri_colour, p2, corner_radius)
pygame.draw.circle(triangle_surf, tri_colour, p3, corner_radius)
pygame.draw.polygon(triangle_surf, tri_colour, [p1, p2, p3])
pygame.draw.polygon(triangle_surf, tri_colour, [p3, p2, p1], width=corner_radius * 2)

triangle_flipped_surf = pygame.transform.flip(triangle_surf, False, True)
x_spacing = (tri_width + gap) // 2
y_spacing = (tri_height + gap)
# question_1_surf = question_font.render("Q1. Whats your favorite color?", True, (255,255,255))

# question_1_surf = subtitle_font.render("Q1. Whats your favorite color?", True, (255,255,255))
# question_1_rect = question_1_surf.get_rect(center=(600,120))

# question_1_1_surf = question_font.render("A. red", True, (255,255,255))
# question_1_1_rect = question_1_1_surf.get_rect(center=(300,310))
# question_1_2_surf = question_font.render("B. blue", True, (255,255,255))
# question_1_2_rect = question_1_2_surf.get_rect(center=(900,310))
# question_1_3_surf = question_font.render("C. green", True, (255,255,255))
# question_1_3_rect = question_1_3_surf.get_rect(center=(300,590))
# question_1_4_surf = question_font.render("D. yellow", True, (255,255,255))
# question_1_4_rect = question_1_4_surf.get_rect(center=(900,590))

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_title = False
                question_1 = True
        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     if question_1_1_rect.collidepoint(event.pos):
        #         pass # will eventually add an amount of personality points and  move to next question
        #     elif question_1_2_rect.collidepoint(event.pos):
        #         pass
        #     elif question_1_3_rect.collidepoint(event.pos):
        #         pass
        #     elif question_1_4_rect.collidepoint(event.pos):
        #         pass
    

   
    current_time = pygame.time.get_ticks()
    

    if game_title == "TITLE": # title screen
        screen.fill((250,170,180))

        for y_count, y in enumerate(range(-tri_height * 2, 900, y_spacing)):
            for x_count, x in enumerate(range(-tri_width * 2, 1300, x_spacing)):
            
                if (x_count + y_count) % 2 == 0:
                    screen.blit(triangle_surf, (x, y))
                else:
                    # y_offset = tri_height // 3 - (gap // 4)
                    screen.blit(triangle_flipped_surf, (x, y + y_spacing // 2))

        screen.blit(title_surf, title_rect)
        if current_time >= 850:  # if the time is past 1 s and then half the time the message is on, half the time its not
            if current_time % 1700 < 850:
                screen.blit(message_surf, message_rect)

    # elif question_1 == True: 
    #     screen.fill((90,100,150))
    #     screen.blit(question_1_surf, question_1_rect)
    #     screen.blit(question_1_1_surf, question_1_1_rect)
    #     screen.blit(question_1_2_surf, question_1_2_rect)
    #     screen.blit(question_1_3_surf, question_1_3_rect)
    #     screen.blit(question_1_4_surf, question_1_4_rect)

    pygame.display.update()
    clock.tick(60)

pygame.quit() 
sys.exit()
