from Graph_utils import *
from Move import *

class Maze:
    def __init__(self, path_maze: str):
        self.Row = 32
        self.Col = 28
        self.map = [[None for _ in range (self.Col)] for _ in range (self.Row)]
        self._load_maze(path_maze)

    def _load_maze(self, path_maze: str):
        with open(path_maze, 'r', encoding='utf-8') as file:
            content = file.readline()
            i = 0
            while content and i < self.Row:
                content = content.strip()
                for j in range (len(content)):
                    if content[j] == '#':
                        self.map[i][j] = -1
                    if content[j] == '.':
                        self.map[i][j] = 1
                    if content[j] == '-':
                        self.map[i][j] = 0
                i = i + 1
                content = file.readline()

    def isWall(self, move: Move, x: int, y: int) -> bool:
        match move:
            case Move.RIGHT:
                return self.map[x+1][y] == -1
            case Move.LEFT:
                return self.map[x-1][y] == -1
            case Move.UP:
                return self.map[x][y-1] == -1
            case Move.DOWN:
                return self.map[x][y+1] == -1
            case _:
                return False

    def hasPellot(self, x: int, y: int) -> bool:
        return self.map[x][y] == 1

    def eatPellot(self, x: int, y: int):
        if self.map[x][y] == 1:
            self.map[x][y] = 0

    def getTile(self, x: int, y: int) -> int:
        return self.map[x][y]