import pygame
import os
import math
from enum import Enum

BoardType = Enum('Type', ['DEFAULT', 'PLAINS', 'RIVERS'])

class Tile():

   def __init__(self, _rows, _cols):
      self.rows = _rows
      self.cols = _cols
      self.type = DEFAULT
      self.tiles[self.cols + self.rows]