import pygame
import os
import math
import transform
import tile
from enum import Enum

BoardType = Enum('Type', ['DEFAULT', 'PLAINS', 'RIVERS'])

class Board():
    def __init__(self, _cols, _rows, width, height, all_tiles_list):
        field_size = min(width, height) / min(_cols, _rows) #px
        self.cols = int(_cols)
        self.rows = int(_rows)
        self.type = BoardType.DEFAULT
        self.tiles = [[tile.Tile(0,0, tile.TileType.DEFAULT, field_size, field_size)] * self.rows] * self.cols

        #init tiles
        for i in range(self.cols):
            self.tiles[i] = [tile.Tile(i,0, tile.TileType.DEFAULT, field_size, field_size)] * self.rows
            for j in range(self.rows):
                self.tiles[i][j] = tile.Tile(i,j, tile.TileType.DEFAULT, field_size, field_size)

        #setup tiles
        for i in range(self.cols):
            for j in range(self.rows):
                tile_inst = self.get_tile(i, j)
                pix_pos = transform.Transform.coord_to_pix(self.cols, self.rows, (tile_inst.view.rect.width, tile_inst.view.rect.height))
                tile_inst.view.rect.x = pix_pos[0] / 2
                tile_inst.view.rect.y = pix_pos[1] / 2
                tile_inst.move(i, j)
                all_tiles_list.add(tile_inst.view)

    def get_tile(self, col, row):
        return self.tiles[col][row]