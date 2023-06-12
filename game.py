import sys
import os
import random
import pygame
import transform
import tmpfigure
import tile
import board

pygame.init()

#defining size of game window
clock = pygame.time.Clock()
window_surface = pygame.display.set_mode((1280,720), pygame.SCALED) #, pygame.FULLSCREEN) 
pygame.display.set_caption("ChessVenture")
pygame.display.toggle_fullscreen()
#pygame.display.set_icon()
#pygame.display.get_window_size()

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
field_width = int(min(board_height, window_surface.get_width()) / 8)
field_height = field_width
board = board.Board(window_surface.get_width() / field_width, 8, window_surface.get_width(), board_height)

transform.Transform.initialize((field_width, field_height), (0, headline_font_size))

figure_width = field_width * 0.9
figure_height = field_height * 0.9
actor = tmpfigure.TmpFigure()
# actor.view.set_offsets((0, headline_font_size), (field_width, field_height))

pix_pos = transform.Transform.coord_to_pix(random.randrange(0,4), random.randrange(0, board.rows), (figure_width, figure_height))
actor.view.rect.x = pix_pos[0]
actor.view.rect.y = pix_pos[1]
# actor.view.rect.x = (random.randrange(0,4) + 0.5) * field_width - figure_width / 2
# actor.view.rect.y = (random.randrange(0,8) + 0.5) * field_height + headline_font_size - figure_height / 2

opponent = tmpfigure.TmpFigure()
opponent.view.set_image(os.path.join('res', 'default_sprite.png'), (figure_width, figure_height), (12, 4))
# opponent.view.set_offsets((0, headline_font_size), (field_width, field_height))

pix_pos = transform.Transform.coord_to_pix(random.randrange(0, board.cols - 4), random.randrange(0,board.rows), (figure_width, figure_height))
opponent.view.rect.x = pix_pos[0]
opponent.view.rect.y = pix_pos[1]
# opponent.view.rect.x = (random.randrange(0,4) + 0.5) * field_width - figure_width / 2
# opponent.view.rect.y = (random.randrange(0,8) + 0.5) * field_height + headline_font_size - figure_height / 2

all_sprites_list = pygame.sprite.Group()
all_tiles_list = pygame.sprite.Group()
all_sprites_list.add(actor.view)
all_sprites_list.add(opponent.view)

for i in range(board.cols):
    for j in range(board.rows):
        tile = board.get_tile(i, j)
        pix_pos = transform.Transform.coord_to_pix(board.cols, board.rows, (tile.view.rect.width, tile.view.rect.height))
        tile.view.rect.x = pix_pos[0] / 2
        tile.view.rect.y = pix_pos[1] / 2
        # tile.rect.x = ((board.cols + 0.5) * field_width - tile.rect.width / 2) / 2
        # tile.rect.y = ((board.rows + 0.5) * field_height + headline_font_size - tile.rect.height / 2) / 2
        # tile.rect.x = ((i + 0.5) * field_size - tile.rect.width / 2) / 2
        # tile.rect.y = ((j + 0.5) * field_size + headline_font_size - tile.rect.width / 2) / 2
        tile.move(i, j)
        all_tiles_list.add(tile.view)

frame_counter = 0

while 1:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:
            if opponent.view.rect.collidepoint(event.pos):
                #transform into board coords in board class
                opponent.on_click(5, 5)

    headline = headline_font.render("ChessVenture ", 1, (255, 0, 255), (255, 255, 255))

    #draw debugbox
    pygame.draw.rect(window_surface, 'black', pygame.Rect(headline.get_width(), 0, window_surface.get_width() - headline.get_width(), headline_font_size))
    
    infobox_text = [
        "current pixel " + str(actor.view.rect.x) + ", " + str(actor.view.rect.y),
        "target pixel " + str(actor.view.target_location.x) + ", " + str(actor.view.target_location.y),
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
            window_surface.blit(labels[line_nr], (headline.get_width() + debugbox_height, line_nr * (debugbox_height + 15)))
        else:
            window_surface.blit(labels[line_nr], (headline.get_width() + max_length + debugbox_height * 2, (line_nr - 3) * (debugbox_height + 15)))
    window_surface.blit(headline, (0, 0))

    #draw fields
    all_tiles_list.update()
    all_tiles_list.draw(window_surface)

    alpha = 10
    white_rect = pygame.Surface((field_width, field_height))
    white_rect.set_alpha(alpha)
    white_rect.fill((255,255,255))
    black_rect = pygame.Surface((field_width, field_height))
    black_rect.set_alpha(alpha)
    black_rect.fill((0,0,0))

    for i in range(board.rows):
        for j in range(board.cols):
            px_row = field_width * i
            px_col = field_height * j

            if((i + j) % 2 == 0):
                window_surface.blit(white_rect, (px_col, px_row + headline_font_size))
            else:
                window_surface.blit(black_rect, (px_col, px_row + headline_font_size))

    #random actions
    if(frame_counter % 300 == 0):
        opponent.move(random.randrange(board.cols - 4, board.cols), random.randrange(0, board.rows))
        actor.move(random.randrange(0,4), random.randrange(0, board.rows))

    #draw all
    all_sprites_list.update(events)
    all_sprites_list.draw(window_surface)
    pygame.display.update()

    frame_counter += 1
    clock.tick(60)