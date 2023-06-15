import os
import random
import transform
import tmpfigure
import tile
import board

class Level():
    def __init__(self, surface_width, surface_height, header_height, all_tiles_list):
        #level assets
        board_height = surface_height - header_height
        field_width = int(min(board_height, surface_width) / 8)
        field_height = field_width

        transform.Transform.initialize((field_width, field_height), (0, header_height))
        
        self.board = board.Board(surface_width / field_width, 8, surface_width, board_height, all_tiles_list)

        #hero
        figure_width = field_width * 0.9
        figure_height = field_height * 0.9
        self.actor = tmpfigure.TmpFigure()

        pix_pos = transform.Transform.coord_to_pix(random.randrange(0,4), random.randrange(0, self.board.rows), (figure_width, figure_height))
        self.actor.view.rect.x = pix_pos[0]
        self.actor.view.rect.y = pix_pos[1]

        #opponent
        self.opponent = tmpfigure.TmpFigure()
        self.opponent.view.set_image(os.path.join('res', 'default_sprite.png'), (figure_width, figure_height), (12, 4))

        pix_pos = transform.Transform.coord_to_pix(random.randrange(0, self.board.cols - 4), random.randrange(0, self.board.rows), (figure_width, figure_height))
        self.opponent.view.rect.x = pix_pos[0]
        self.opponent.view.rect.y = pix_pos[1]
        return

    def update(self, frame_counter):
        #random actions
        if(frame_counter % 300 == 0):
            self.opponent.move(random.randrange(self.board.cols - 4, self.board.cols), random.randrange(0, self.board.rows))
            self.actor.move(random.randrange(0,4), random.randrange(0, self.board.rows))
        return

    def update_visuals(self):
        return