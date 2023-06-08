import sys
import random
import pygame
import tmpfigure

pygame.init()

#defining size of game window
clock = pygame.time.Clock()
window_surface = pygame.display.set_mode((800,600)) 
pygame.display.set_caption("ChessVenture")

#defining font attributes
font_size = 90
infobox_height = 12
headline_font = pygame.font.SysFont("Segoe UI", font_size)
infobox_font = pygame.font.SysFont("Segoe UI", infobox_height)
headline = headline_font.render("ChessVenture", 1, (255, 0, 255), (255, 255, 255))
font_size = headline.get_height()
infobox = infobox_font.render("Infobox", 1, 'white')
    
#game assets
board_height = window_surface.get_height() - font_size
field_size = min(board_height, window_surface.get_width()) / 8

actor_width = 20
actor = tmpfigure.TmpFigure(actor_width, actor_width)
actor.rect.x = random.randrange(0,4) * field_size + field_size * 0.5 - actor_width / 2
actor.rect.y = random.randrange(0,8) * field_size + field_size * 0.5 + font_size - actor_width / 2
# actor.set_

all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(actor)

frame_counter = 0

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: sys.exit()

    headline = headline_font.render("ChessVenture ", 1, (255, 0, 255), (255, 255, 255))
    infobox_text = [
        "current pixel " + str(actor.rect.x) + ", " + str(actor.rect.y),
        "target pixel " + str(actor.target_location.x) + ", " + str(actor.target_location.y),
        "target field " + str(actor.col) + ", " + str(actor.row),
        "target field " + str(actor.target_location.x) + ", " + str(actor.target_location.y)
    ]
    labels = []
    for line in infobox_text:
        labels.append(infobox_font.render(line, 1, 'white', 'black'))
        
    for line_nr in range(len(labels)):
        window_surface.blit(labels[line_nr], (headline.get_width(), line_nr * (infobox_height + 15)))
    # for label in labels:
    #     window_surface.blit(label, (headline.get_width(), infobox_height))
    window_surface.blit(headline, (0, 0))

    #draw fields
    for i in range(8):
        for j in range(int(window_surface.get_width() / field_size)):
            row = field_size * i
            col = field_size * j
            if((i + j) % 2 == 0):
                color = 'white'
            else:
                color = 'black'
            pygame.draw.rect(window_surface, color, pygame.Rect(col, row + font_size, field_size, field_size))

    if(frame_counter % 300 == 0):
        actor.move(random.randrange(0,4),random.randrange(0,8), field_size, font_size)
    all_sprites_list.update()
    all_sprites_list.draw(window_surface)
    pygame.display.update()

    frame_counter += 1
    clock.tick(60)