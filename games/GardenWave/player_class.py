import pygame as py
import game_window_class

class Player():
    def __init__(self, x , y , way):
        self.avatar = py.image.load(way).convert_alpha()
        self.coordinate_X = x
        self.coordinate_Y = y
        self.last_coor_x = x
        self.last_coor_y = y
        self.key = py.key.get_pressed()
        self.score = 10
        self.font = py.font.Font(None, 32)
        self.text_score = self.font.render(f"Score:{self.score}",False, 'white'  )

