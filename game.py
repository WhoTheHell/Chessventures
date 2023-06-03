import sys
import pygame
pygame.init()

#defining size of game window
window = pygame.display.set_mode((800,600)) 
pygame.display.set_caption("Hello World Printer")

#defining font attributes
font_size = 90
headline_font = pygame.font.SysFont("Segoe UI", font_size)
headline = headline_font.render("ChessVenture", 1, (255, 0, 255), (255, 255, 255))

while 1:
    for event in pygame.event.get():
        if event.type==pygame.QUIT: sys.exit()

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

    window.blit(headline, (0, 0))
    pygame.display.update()