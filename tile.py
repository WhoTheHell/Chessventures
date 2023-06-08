import pygame
from pygame.rect import Rect
import os
import math
from enum import Enum

TileType = Enum('Type', ['DEFAULT', 'GREENS', 'WATER'])

class Tile(pygame.sprite.Sprite):

   def __init__(self, width, height):
      super().__init__()

      self.image = pygame.image.load(os.path.join('res', 'dirt_0.jpg'))
      self.image = pygame.transform.scale(self.image, (width, height))

      self.rect = self.image.get_rect()
      self.row = 0
      self.col = 0
      self.type = DEFAULT

   def update(self):
        self
        #do something