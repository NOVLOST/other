import pygame as py

class GameWin():
    def __init__(self,x,y,background,r,g,b):
        self.display_set_mode = py.display.set_mode((x,y))
        self.background = py.image.load(background).convert_alpha()
        # self.win_blit = self.display_set_mode.blit(self.background, (0, 0))
        self.border_right = py.draw.line(self.display_set_mode, (r, g, b), (800, 0), (800, 600), 3)
        self.border_left = py.draw.line(self.display_set_mode, (r, g, b), (0, 0), (0, 600), 3)
        self.border_up = py.draw.line(self.display_set_mode, (r, g, b), (0, 0), (800, 0), 3)
        self.border_down = py.draw.line(self.display_set_mode, (r, g, b), (0, 600), (800, 600), 3)