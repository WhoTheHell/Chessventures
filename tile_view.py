import pygame
from pygame.rect import Rect
import os
import math
import transform
import tmpfigure
from enum import Enum

class TileView(pygame.sprite.Sprite):
    figure: tmpfigure.TmpFigure

    def __init__(self, path, width = 50, height = 50):
        super().__init__()

        self.image = pygame.image.load(path)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.move_speed = 2 #pixel per frame

        self.rect = self.image.get_rect()
        self.target_location = Rect(self.rect)

    def update(self):
        self.update_pos()

    def update_pos(self):
        if(self.rect.x == self.target_location.x and self.rect.y == self.target_location.y):
            return

        x_dist = self.rect.x - self.target_location.x
        y_dist = self.rect.y - self.target_location.y
        euklidean_dist = math.sqrt(x_dist * x_dist + y_dist * y_dist)

        if(euklidean_dist <= self.move_speed): #FIXME why does this produce gaps and overlappings?
            self.rect.x = self.target_location.x
            self.rect.y = self.target_location.y
            return

        ratio = euklidean_dist / self.move_speed
        bow = (0.05815 * math.sqrt(euklidean_dist)) ** 2
        new_x_increment = x_dist / ratio
        new_y_increment = y_dist / ratio + bow

        self.rect.x -= new_x_increment
        self.rect.y -= new_y_increment

    def move(self, _col, _row):
        pix_pos = transform.Transform.coord_to_pix(_col, _row, (self.image.get_width() / 2, self.image.get_height() / 2))
        self.target_location.x = pix_pos[0]
        self.target_location.y = pix_pos[1]
        # self.target_location.x = (self.col + 0.5) * offset - self.image.get_width() / 2
        # self.target_location.y = (self.row + 0.5) * offset + header_row - self.image.get_width() / 2