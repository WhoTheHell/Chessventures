import tmpfigure_view
import os

class TmpFigure():

   def __init__(self, path = None, _col = 0, _row = 0):
      super().__init__()
      
      self.col = _col
      self.row = _row

      if path == None:
         path = os.path.join('res', 'strawberry.jpg')
      self.image_path = path
      self.view = tmpfigure_view.TmpFigureView(path)

   def update(self, events):
      self.view.update(events)

   def move(self, _col, _row):
      #TODO call host_figure on tile
      self.col = _col
      self.row = _row
      self.view.move(_col, _row)

   def on_click(self, _col, _row):
      self.move(_col, _row)