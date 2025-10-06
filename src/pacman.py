from move import *

class Pacman:
    def __init__(self, start_pos):
        self.position = start_pos
        self.direction = (0,0)
        self.score = 0

    #teste