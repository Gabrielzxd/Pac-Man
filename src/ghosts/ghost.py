from modes import *

class Ghost:
    def __init__(self, x, y, mode):
        self.x = x
        self.y = y
        self.mode = Mode.SCATTER

    # def update

    def change_mode(self, new_mode):
        self.mode = new_mode

