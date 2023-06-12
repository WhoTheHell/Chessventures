import pygame
from pygame.rect import Rect
import os
import math
import transform
import tile_view
import tmpfigure
from enum import Enum

TileType = Enum('Type', ['DEFAULT', 'GREENS', 'WATER'])

class Tile():
    figure: tmpfigure.TmpFigure #instance var. type annotation https://peps.python.org/pep-0526/#class-and-instance-variable-annotations

    def __init__(self, _col, _row, _type, width, height, _path = None):
        super().__init__()

        self.col = _col
        self.row = _row
        self.type = _type

        if _path == None:
            if _type == TileType.DEFAULT:
                _path = os.path.join('res', 'dirt_0.png')
        self.image_path = _path
        self.view = tile_view.TileView(_path, width, height)

    def update(self):
        self.view.update()

    def move(self, _col, _row):
        self.col = _col
        self.row = _row
        self.view.move(_col, _row)

    def host_figure(self, fig):
        if(self.figure == Null):
            self.figure = fig
            return True
        else:
            return False