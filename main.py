import pygame # imma try make this in pygame
import sys
import math

#setup
pygame.init()
screen = pygame.display.set_mode ((1200,800))
pygame.display.set_caption("Personality Test")
clock = pygame.time.Clock()


game_title = "TITLE"
question_1 = False
running = True

personility_score_red = 0
personility_score_blue = 0
personility_score_green = 0
personility_score_yellow = 0

title_font = pygame.font.Font('fonts/gorditas.ttf', 120)
subtitle_font = pygame.font.Font('fonts/gorditas.ttf', 70)
question_font = pygame.font.Font('fonts/gorditas.ttf', 50)

#surfaces rest will be generated during the game 
title_surf = title_font.render("Personality Test", True, (255,255,255))
title_rect = title_surf.get_rect(center=(600,300))

message_surf = question_font.render("(press space to start)", True, (255,255,255))
message_rect = message_surf.get_rect(center=(600,550))


#questions
class question:
    def __init__(self, question_text, answer_1, answer_2, answer_3, answer_4):
        self.question_text = question_text
        self.answer_1 = answer_1
        self.answer_2 = answer_2
        self.answer_3 = answer_3
        self.answer_4 = answer_4

    def select_answer(self, answerChoice):
        global personality_score_red, personality_score_blue, personality_score_green, personality_score_yellow
        if answerChoice == self.answer_1:
            personality_score_red += 1
        elif answerChoice == self.answer_2:
            personality_score_blue += 1
        elif answerChoice == self.answer_3:
            personality_score_green += 1
        elif answerChoice == self.answer_4:
            personality_score_yellow += 1

    def get_question_text(self):
        return self.question_text

    def get_answerList(self):
        return [self.answer_1, self.answer_2, self.answer_3, self.answer_4]

question1 = question("Q1. Whats your favorite color?", "red", "blue", "green", "yellow")
question2 = question("Q2. Whats your favorite animal?", "cat", "dog", "horse", "fish")
question3 = question("Q3. Whats your favorite food?", "pizza", "ice cream", "burger", "sushi")
question4 = question("Q4. Whats your favorite drink?", "coffee", "tea", "beer", "water")

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

def createSurfaces(question):
    title_surf_local = title_font.render("Personality Test", True, (255,255,255))
    title_rect_local = title_surf_local.get_rect(center=(600,300))

    message_surf_local = question_font.render("(press space to start)", True, (255,255,255))
    message_rect_local = message_surf_local.get_rect(center=(600,550))

    question_1_surf_local = subtitle_font.render(question.get_question_text(), True, (255,255,255))
    question_1_rect_local = question_1_surf_local.get_rect(center=(600,120))

    answer_1_surf = question_font.render(question.get_answerList()[0], True, (255,255,255))
    answer_1_rect = answer_1_surf.get_rect(center=(300,310))
    answer_2_surf = question_font.render(question.get_answerList()[1], True, (255,255,255))
    answer_2_rect = answer_2_surf.get_rect(center=(900,310))
    answer_3_surf = question_font.render(question.get_answerList()[2], True, (255,255,255))
    answer_3_rect = answer_3_surf.get_rect(center=(300,590))
    answer_4_surf = question_font.render(question.get_answerList()[3], True, (255,255,255))
    answer_4_rect = answer_4_surf.get_rect(center=(900,590))

    return (
        title_surf_local,
        title_rect_local,
        message_surf_local,
        message_rect_local,
        question_1_surf_local,
        question_1_rect_local,
        answer_1_surf,
        answer_1_rect,
        answer_2_surf,
        answer_2_rect,
        answer_3_surf,
        answer_3_rect,
        answer_4_surf,
        answer_4_rect,
    )

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

    elif question_1 == True: 
        screen.fill((180,110,110))
        question_surfaces = createSurfaces(question1)
        screen.blit(question_surfaces[4], question_surfaces[5])
        screen.blit(question_surfaces[6], question_surfaces[7])
        screen.blit(question_surfaces[8], question_surfaces[9])
        screen.blit(question_surfaces[10], question_surfaces[11])
        screen.blit(question_surfaces[12], question_surfaces[13])

    pygame.display.update()
    clock.tick(60)

pygame.quit() 
sys.exit()