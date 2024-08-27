import pygame as py

class Plant():
    def __init__(self,x,y,time,i):
        self.skin_index = i
        self.skin_list = f'image/wild_plant_grow_{self.skin_index}.png'
        self.skin = py.image.load(self.skin_list).convert_alpha()
        self.coordinate_X = x
        self.coordinate_Y = y
        self.grow_time = time
        self.show = self.skin.get_rect(topleft=(self.coordinate_X, self.coordinate_Y))
