import pygame # imma try make this in pygame
import sys
import math

#setup for window
pygame.init()
screen = pygame.display.set_mode ((1200,800))
pygame.display.set_caption("Personality Test")
clock = pygame.time.Clock()

#start variables 
game_state = "TITLE"
running = True
current_question_index = 0
score = {
    'red' : 0,
    'blue' : 0,
    'green' : 0,
    'yellow' : 0
}
# font setup
title_font = pygame.font.Font('fonts/gorditas.ttf', 120)
subtitle_font = pygame.font.Font('fonts/gorditas.ttf', 63)
answer_font = pygame.font.Font('fonts/gorditas.ttf', 50)

# only text that isnt autoamticlaly generated  
title_surf = title_font.render("Personality Test", True, (255,255,255))
title_rect = title_surf.get_rect(center=(600,300))
message_surf = answer_font.render("(press space to start)", True, (255,255,255))
message_rect = message_surf.get_rect(center=(600,510))


#questions for quiz, as many as u want
question_list = [
    {
        'question': 'Whats your favourite colour?', 
        'answers': [
            {'text':'Red', 'points': {'red' : 1, 'blue' : 0, 'green' : 0, 'yellow' : 0}},
            {'text':'Blue', 'points': {'red' : 0, 'blue' : 1, 'green' : 0, 'yellow' : 0}},
            {'text':'Green', 'points': {'red' : 0, 'blue' : 0, 'green' : 1, 'yellow' : 0}},
            {'text':'Yellow', 'points': {'red' : 0, 'blue' : 0, 'green' : 0, 'yellow' : 1}}
        ]
    },

    {
        'question': 'Whats your favourite animal?',
        'answers': [
            {'text':'Cat', 'points': {'red' : 0, 'blue' : 0, 'green' : 0, 'yellow' : 0}},
            {'text':'Dog', 'points': {'red' : 0, 'blue' : 0, 'green' : 0, 'yellow' : 0}},
            {'text':'Horse', 'points': {'red' : 0, 'blue' : 0, 'green' : 0, 'yellow' : 0}},
            {'text':'Fish', 'points': {'red' : 0, 'blue' : 0, 'green' : 0, 'yellow' : 0}},
        ]
    },

    {
        'question': 'Whos your favourite Terra NPC?',
        'answers': [
            {'text':'Poobert', 'points': {'red' : 0, 'blue' : 0, 'green' : 0, 'yellow' : 0}},
            {'text':'Ratticus', 'points': {'red' : 0, 'blue' : 0, 'green' : 0, 'yellow' : 0}},
            {'text':'Heidi', 'points': {'red' : 0, 'blue' : 0, 'green' : 0, 'yellow' : 0}},
            {'text':'Blargh', 'points': {'red' : 0, 'blue' : 0, 'green' : 0, 'yellow' : 0}},
        
        ]
    },

    {
        'question': 'Do you like your terra?',
        'answers': [
            {'text':'Yes', 'points': {'red' : 0, 'blue' : 0, 'green' : 0, 'yellow' : 0}},
            {'text':'Yes', 'points': {'red' : 0, 'blue' : 0, 'green' : 0, 'yellow' : 0}},
            {'text':'Yes', 'points': {'red' : 0, 'blue' : 0, 'green' : 0, 'yellow' : 0}},
            {'text':'Yes', 'points': {'red' : 0, 'blue' : 0, 'green' : 0, 'yellow' : 0}},
        ]
    },

    {
        'question': 'Whats your fav coding language?',
        'answers': [
            {'text':'Python', 'points': {'red' : 0, 'blue' : 0, 'green' : 0, 'yellow' : 0}},
            {'text':'Java', 'points': {'red' : 0, 'blue' : 0, 'green' : 0, 'yellow' : 0}},
            {'text':'C#', 'points': {'red' : 0, 'blue' : 0, 'green' : 0, 'yellow' : 0}},
            {'text':'C++', 'points': {'red' : 0, 'blue' : 0, 'green' : 0, 'yellow' : 0}},
        ]
    }

]


#title page bg function means i can minimise it makes code look cleaner
def bg(r, g, b):
    tri_width = 140
    tri_height = int(tri_width * (math.sqrt(3)/2))
    corner_radius = 16
    gap = 80
    tri_colour = (r, g, b)

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
    for y_count, y in enumerate(range(-tri_height * 2, 900, y_spacing)):
                for x_count, x in enumerate(range(-tri_width * 2, 1300, x_spacing)):
                
                    if (x_count + y_count) % 2 == 0:
                        screen.blit(triangle_surf, (x, y))
                    else:
                        # y_offset = tri_height // 3 - (gap // 4)
                        screen.blit(triangle_flipped_surf, (x, y + y_spacing // 2))
    return screen #not sure if i need this but i donesnt do anything rn
    
    
# functions to automactically generate the ui for the quiz based on what question we are on
def current_quiz_ui(index):
    q_data = question_list[index]
    q_surf = subtitle_font.render(q_data['question'], True, (255,255,255))
    q_rect = q_surf.get_rect(center=(600,150))

    positions = [(300,380), (900,380), (300,600), (900,600)]
    answers_surf = []
    answers_rect = []

    for i, ans in enumerate(q_data['answers']):
        surf = answer_font.render(ans['text'], True, (255,255,255))
        rect = surf.get_rect(center=positions[i])
        answers_surf.append(surf)
        answers_rect.append(rect)

    return (
        q_surf,
        q_rect,
        answers_surf,
        answers_rect,
    )

# actual main game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_state = "QUIZ"
                current_question_index = 0
                score = {k: 0 for k in score}
        # need to add mouse collision detection
        if event.type == pygame.MOUSEBUTTONDOWN and game_state == "QUIZ":
            _,_,_, ans_rect = current_quiz_ui(current_question_index)
            for i, rect in enumerate(ans_rect):
                if rect.collidepoint(event.pos):
                    answer_points = question_list[current_question_index]['answers'][i]['points']
                    for colour in score:
                        score[colour] += answer_points.get(colour, 0)
                    if current_question_index < len(question_list) - 1:
                        current_question_index += 1
                    else:
                        game_state = "RESULTS"
                    break
    current_time = pygame.time.get_ticks()

    # code for each state, will automatically cycle through after each event
    if game_state == "TITLE": # title screen  
        screen.fill((250,170,180))
        bg(250, 160, 170)
        screen.blit(title_surf, title_rect)
        if current_time >= 850:  # (blinking text)if the time is past 1 s and then half the time the message is on, half the time its not
            if current_time % 1700 < 850:
                screen.blit(message_surf, message_rect)

    elif game_state == "QUIZ":
        screen.fill((170,200,250)) # might make a different colour for each question and make custom bg
        bg(164, 194, 250)
        q_surf, q_rect, ans_surf, ans_rect = current_quiz_ui(current_question_index)
        screen.blit(q_surf, q_rect)
        for surf, rect in zip(ans_surf, ans_rect):
            pygame.draw.rect(screen, (255,255,255), rect.inflate(30, 20), width=5, border_radius=10)
            screen.blit(surf, rect)

    elif game_state == "RESULTS":
        pass #placeholder

    pygame.display.update()
    clock.tick(60)

pygame.quit() 
sys.exit()