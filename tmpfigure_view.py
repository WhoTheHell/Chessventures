import pygame
from pygame.rect import Rect
import math
import transform

class TmpFigureView(pygame.sprite.Sprite):

   def __init__(self, path, width = 50, height = 50):
      super().__init__()

      self.move_speed = 2 #pixel per frame

      self.animation = []
      self.frame_counter = 0
      self.sprite_cols = 0
      self.sprite_rows = 0
      self.sprite_col = 0
      self.sprite_row = 0
      self.set_image(path, (width, height))
      self.rect = self.image.get_rect()
      self.target_location = Rect(self.rect)
      # self.static_offset = _static_offset
      # self.raster_size = _raster_size

   def update(self, events):
      self.update_pos()
      if len(self.animation) != 0:
         self.iterate_sprite()
      for event in events:
         if event.type == pygame.MOUSEBUTTONUP:
            if self.rect.collidepoint(event.pos):
               self.on_click()

   def update_pos(self):
      if(self.rect.x == self.target_location.x and self.rect.y == self.target_location.y):
         return

      x_dist = self.rect.x - self.target_location.x
      y_dist = self.rect.y - self.target_location.y
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

   def move(self, _col, _row):
      pix_pos = transform.Transform.coord_to_pix(_col, _row, (self.image.get_width() / 2, self.image.get_height() / 2))
      self.target_location.x = pix_pos[0]
      self.target_location.y = pix_pos[1]
      # self.target_location.x = self.static_offset[0] + (_col + 0.5) * self.raster_size[0] - self.image.get_width() / 2
      # self.target_location.y = self.static_offset[1] + (_row + 0.5) * self.raster_size[1] - self.image.get_height() / 2

   # def set_offsets(self, _static_offset, _raster_size):
   #    self.static_offset = _static_offset
   #    self.raster_size = _raster_size

   def set_image(self, path, size = None, cols_rows = None): #assume sheet if cols_rows is given
      if size == None:
         size = (self.rect.width, self.rect.height)
      self.image = pygame.image.load(path)
      
      if cols_rows != None:
         self.sprite_cols = cols_rows[0]
         self.sprite_rows = cols_rows[1]
         self.sprite_col = 0
         self.sprite_row = 0
         self.animation = [ [pygame.Surface] * self.sprite_rows for i in range(self.sprite_cols) ]
         width = self.image.get_rect().width / self.sprite_cols
         height = self.image.get_rect().height / self.sprite_rows
         for col in range(self.sprite_cols):
            for row in range(self.sprite_rows):
               x = col * width
               y = row * height
               cropping_region = (x, y, width, height)
               self.animation[col][row] = self.image.subsurface(cropping_region)
         self.image = self.animation[self.sprite_col][self.sprite_row]

      self.image = pygame.transform.scale(self.image, size)

   def on_click(self):
      self.move(5, 5)

   def iterate_sprite(self):
      if self.frame_counter % 10 == 0:
         self.sprite_col += 1
         if self.sprite_col >= self.sprite_cols:
            self.sprite_col = 0
            self.sprite_row += 1
            if self.sprite_row >= self.sprite_rows:
               self.sprite_row = 0
         self.image = self.animation[self.sprite_col][self.sprite_row]
      self.frame_counter += 1