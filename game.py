import sys
import os
import random
import pygame
import level
import board

###global variable space

pygame.init()
clock = pygame.time.Clock()
#defining size of game window
window_surface = pygame.display.set_mode((1280,720), pygame.SCALED) #, pygame.FULLSCREEN) 

#defining font attributes
headline_font_size = 60
headline_font = pygame.font.SysFont("Segoe UI", headline_font_size)
headline = headline_font.render("ChessVenture", 1, (255, 0, 255), (255, 255, 255))
headline_font_size = headline.get_height()

debugbox_height = 12
debugbox_font = pygame.font.SysFont("Segoe UI", debugbox_height)
debugbox_col_length = 0

all_sprites_list = pygame.sprite.Group()
all_tiles_list = pygame.sprite.Group()

stage = level.Level(window_surface.get_width(), window_surface.get_height(), headline_font_size, all_tiles_list)

###functions

def setup():
    pygame.display.set_caption("ChessVenture")
    pygame.display.toggle_fullscreen()
    #pygame.display.set_icon()
    #pygame.display.get_window_size()
    all_sprites_list.add(stage.actor.view)
    all_sprites_list.add(stage.opponent.view)

def update_loop():
    frame_counter = 0
    while 1:
        #collisions etc
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                if opponent.view.rect.collidepoint(event.pos):
                    #transform into board coords in board class
                    opponent.on_click(5, 5)

        #update modelcontrols
        stage.update(frame_counter)

        #update and draw all visuals
        stage.update_visuals()

        headline = headline_font.render("ChessVenture ", 1, (255, 0, 255), (255, 255, 255))

        #draw debugbox
        pygame.draw.rect(window_surface, 'black', pygame.Rect(headline.get_width(), 0, window_surface.get_width() - headline.get_width(), headline_font_size))
        
        infobox_text = [
            "current pixel " + str(stage.actor.view.rect.x) + ", " + str(stage.actor.view.rect.y),
            "target pixel " + str(stage.actor.view.target_location.x) + ", " + str(stage.actor.view.target_location.y),
            "target field " + str(stage.actor.col) + ", " + str(stage.actor.row),
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

        #if behaviour of tile_view is changed integrate this as a blit on the tile surface inside board
        alpha = 10
        field_width = stage.board.tiles[0][0].view.rect.width
        field_height = stage.board.tiles[0][0].view.rect.height
        white_rect = pygame.Surface((field_width, field_height))
        white_rect.set_alpha(alpha)
        white_rect.fill((255,255,255))
        black_rect = pygame.Surface((field_width, field_height))
        black_rect.set_alpha(alpha)
        black_rect.fill((0,0,0))

        for i in range(stage.board.rows):
            for j in range(stage.board.cols):
                px_row = field_width * i
                px_col = field_height * j

                if((i + j) % 2 == 0):
                    window_surface.blit(white_rect, (px_col, px_row + headline_font_size))
                else:
                    window_surface.blit(black_rect, (px_col, px_row + headline_font_size))

        #draw all
        all_sprites_list.update(events)
        all_sprites_list.draw(window_surface)
        pygame.display.update()

        frame_counter += 1
        clock.tick(60)

if __name__ == "__main__":
    setup()
    update_loop()