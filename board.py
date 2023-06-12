import pygame
import os
import math
import tile
from enum import Enum

BoardType = Enum('Type', ['DEFAULT', 'PLAINS', 'RIVERS'])

class Board():

    def __init__(self, _cols, _rows, width, height):
        field_size = min(width, height) / min(_cols, _rows) #px
        self.cols = int(_cols)
        self.rows = int(_rows)
        self.type = BoardType.DEFAULT
        self.tiles = [[tile.Tile(0,0, tile.TileType.DEFAULT, field_size, field_size)] * self.rows] * self.cols

        for i in range(self.cols):
            self.tiles[i] = [tile.Tile(i,0, tile.TileType.DEFAULT, field_size, field_size)] * self.rows
            for j in range(self.rows):
                self.tiles[i][j] = tile.Tile(i,j, tile.TileType.DEFAULT, field_size, field_size)

    def get_tile(self, col, row):
        return self.tiles[col][row]