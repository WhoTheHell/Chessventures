import sys
import random
import pygame
import tmpfigure

pygame.init()

#defining size of game window
window = pygame.display.set_mode((800,600)) 
pygame.display.set_caption("ChessVenture")

#defining font attributes
font_size = 90
headline_font = pygame.font.SysFont("Segoe UI", font_size)
headline = headline_font.render("ChessVenture", 1, (255, 0, 255), (255, 255, 255))
font_size = headline.get_height()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: sys.exit()

    #draw fields
    board_height = window.get_height() - font_size
    field_size = min(board_height, window.get_width()) / 8
    for i in range(8):
        for j in range(int(window.get_width() / field_size)):
            row = field_size * i
            col = field_size * j
            if((i + j) % 2 == 0):
                color = 'white'
            else:
                color = 'black'
            pygame.draw.rect(window, color, pygame.Rect(col, row + font_size, field_size, field_size))

    actor_width = 20
    actor = figure.TmpFigure('red', actor_width, actor_width)
    actor.rect.x = random.randrange(0,4) * field_size + field_size * 0.5 - actor_width / 2
    actor.rect.y = random.randrange(0,8) * field_size + field_size * 0.5 + font_size - actor_width / 2

    all_sprites_list = pygame.sprite.Group(actor)
   # all_sprites_list.add(figure)

    all_sprites_list.draw(window)

    window.blit(headline, (0, 0))
    pygame.display.update()

    clock = pygame.time.Clock()
    clock.tick(60)