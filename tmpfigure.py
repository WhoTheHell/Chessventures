import pygame
from pygame.rect import Rect
import os
import math

class TmpFigure(pygame.sprite.Sprite):

   def __init__(self, width, height):
      super().__init__()

      self.image = pygame.image.load(os.path.join('res', 'strawberry.jpg'))
      self.image = pygame.transform.scale(self.image, (width, height))
      self.move_speed = 2 #pixel per frame

      self.rect = self.image.get_rect()
      self.target_location = Rect(self.rect)
      self.row = 0
      self.col = 0

   def update(self):
      self.update_pos()

   def update_pos(self):
      if(self.rect.x == self.target_location.x and self.rect.y == self.target_location.y):
         return

      x_dist = self.rect.x - self.target_location.x
      y_dist = self.rect.y - self.target_location.y
      # slope = x_dist / y_dist
      euklidean_dist = math.sqrt(x_dist * x_dist + y_dist * y_dist)

      if(euklidean_dist <= self.move_speed):
         self.rect.x = self.target_location.x
         self.rect.y = self.target_location.y
         return

      ratio = euklidean_dist / self.move_speed
      new_x_increment = x_dist / ratio
      new_y_increment = y_dist / ratio

      self.rect.x -= new_x_increment
      self.rect.y -= new_y_increment

   def move(self, _col, _row, offset, header_row):
      #todo missing field_size
      self.col = _col
      self.row = _row
      self.target_location.x = self.col * offset + offset * 0.5 - self.image.get_width() / 2
      self.target_location.y = self.row * offset + offset * 0.5 + header_row - self.image.get_width() / 2