import pygame
import os
import math
import tile
from enum import Enum

BoardType = Enum('Type', ['DEFAULT', 'PLAINS', 'RIVERS'])

class Board():

   def __init__(self, _cols, _rows, field_size):
      self.cols = int(_cols)
      self.rows = int(_rows)
      self.type = BoardType.DEFAULT
      self.tiles = [[tile.Tile(field_size, field_size)] * self.cols] * self.rows