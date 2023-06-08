import sys
import random
import pygame
import tmpfigure
import tile
import board

pygame.init()

#defining size of game window
clock = pygame.time.Clock()
window_surface = pygame.display.set_mode((800,600)) 
pygame.display.set_caption("ChessVenture")

#defining font attributes
headline_font_size = 60
headline_font = pygame.font.SysFont("Segoe UI", headline_font_size)
headline = headline_font.render("ChessVenture", 1, (255, 0, 255), (255, 255, 255))
headline_font_size = headline.get_height()

debugbox_height = 12
debugbox_font = pygame.font.SysFont("Segoe UI", debugbox_height)
debugbox_col_length = 0
    
#game assets
board_height = window_surface.get_height() - headline_font_size
field_size = min(board_height, window_surface.get_width()) / 8
board = board.Board(field_size, 8, int(window_surface.get_width() / field_size))

actor_width = 20
actor = tmpfigure.TmpFigure(actor_width, actor_width)
actor.rect.x = random.randrange(0,4) * field_size + field_size * 0.5 - actor_width / 2
actor.rect.y = random.randrange(0,8) * field_size + field_size * 0.5 + headline_font_size - actor_width / 2

all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(actor)

frame_counter = 0

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: sys.exit()

    headline = headline_font.render("ChessVenture ", 1, (255, 0, 255), (255, 255, 255))

    #draw debugbox
    pygame.draw.rect(window_surface, 'black', pygame.Rect(headline.get_width(), 0, headline.get_width(), headline_font_size))
    
    infobox_text = [
        "current pixel " + str(actor.rect.x) + ", " + str(actor.rect.y),
        "target pixel " + str(actor.target_location.x) + ", " + str(actor.target_location.y),
        "target field " + str(actor.col) + ", " + str(actor.row),
        "game tick " + str(frame_counter)
    ]

    labels = []
    for line in infobox_text:
        labels.append(debugbox_font.render(line, 1, 'white'))
    
    max_length = 0
    for line_nr in range(len(labels)):
        if(line_nr <= 2):
            max_length = max(labels[line_nr].get_width(), max_length)
            window_surface.blit(labels[line_nr], (headline.get_width(), line_nr * (debugbox_height + 15)))
        else:
            window_surface.blit(labels[line_nr], (headline.get_width() + max_length + debugbox_height, (line_nr - 3) * (debugbox_height + 15)))
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
            pygame.draw.rect(window_surface, color, pygame.Rect(col, row + headline_font_size, field_size, field_size))

    if(frame_counter % 300 == 0):
        actor.move(random.randrange(0,4),random.randrange(0,8), field_size, headline_font_size)
    all_sprites_list.update()
    all_sprites_list.draw(window_surface)
    pygame.display.update()

    frame_counter += 1
    clock.tick(60)