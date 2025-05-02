import pygame as py


class Player():
    def __init__(self,connect,addr,start_x ,start_y,way ):
        self.connection = connect
        self.addr = addr
        self.avatar = py.image.load(way).convert_alpha()
        self.speed = 5
        self.vector = [0,0]
        self.coordinate_X = start_x
        self.coordinate_Y = start_y
        self.connection_errors = 0
        self.key = py.key.get_pressed()

