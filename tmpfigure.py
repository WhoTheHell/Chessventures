import pygame
from pygame.rect import Rect
import os
import math

class TmpFigure(pygame.sprite.Sprite):

   def __init__(self, width, height):
      super().__init__()

      self.move_speed = 2 #pixel per frame

      self.animation = []
      self.set_image(os.path.join('res', 'strawberry.jpg'), (width, height))
      self.rect = self.image.get_rect()
      self.target_location = Rect(self.rect)
      self.col = 0
      self.row = 0

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
      #TODO call host_figure on tile
      self.col = _col
      self.row = _row
      self.target_location.x = (self.col + 0.5) * offset - self.image.get_width() / 2
      self.target_location.y = (self.row + 0.5) * offset + header_row - self.image.get_width() / 2

   def set_image(self, path, size = None, cols_rows = None):
      if size == None:
         size = (self.rect.width, self.rect.height)
      self.image = pygame.image.load(path)
      
      if cols_rows != None:
         self.animation = [ [pygame.Surface] * cols_rows[1] for i in range(cols_rows[0]) ]
         width = self.image.get_rect().width / cols_rows[0]
         height = self.image.get_rect().height / cols_rows[1]
         for col in range(cols_rows[0]):
            for row in range(cols_rows[1]):
               x = col * width
               y = row * height
               cropping_region = (x, y, width, height)
               self.animation[col][row] = self.image.subsurface(cropping_region)
         self.image = self.animation[0][0]

      self.image = pygame.transform.scale(self.image, size)