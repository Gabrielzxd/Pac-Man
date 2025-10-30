from src.utils.graph import Graph
from player.move import *

class Maze:
    def __init__(self, path_maze: str):
        self.Row = 31
        self.Col = 28
        self.map = [[None for _ in range (self.Col)] for _ in range (self.Row)]
        self._load_maze(path_maze)

    def _load_maze(self, path_maze: str):
        with open(path_maze, 'r', encoding='utf-8') as file:
            content = file.readline()
            i = 0
            while content and i < self.Row:
                for j in range (len(content)):
                    if content[j] == '#':
                        self.map[i][j] = -1
                    if content[j] == '.':
                        self.map[i][j] = 1
                    if content[j] == '-':
                        self.map[i][j] = 0
                    if content[j] == '+':
                        self.map[i][j] = 2
                i = i + 1
                content = file.readline()

    def create_graph(self):
        graph = Graph()
        for i in range(self.Row):
            for j in range(self.Col):
                if self.map[i][j] == 1 or self.map[i][j] == 0:
                    graph.add_node((i, j), i, j)
                    if i + 1 < self.Row and (self.map[i+1][j] in (0, 1, 2)):
                        graph.add_edge((i, j), (i + 1, j))
                    if i - 1 >= 0 and (self.map[i-1][j] in (0, 1, 2)):
                        graph.add_edge((i, j), (i - 1, j))
                    if j + 1 < self.Col and (self.map[i][j+1] in (0, 1, 2)):
                        graph.add_edge((i, j), (i, j + 1))
                    if j - 1 >= 0 and (self.map[i][j-1] in (0, 1, 2)):
                        graph.add_edge((i, j), (i, j - 1))
        return graph

    def is_wall(self, move: Move, x: int, y: int):
        match move:
            case move.RIGHT:
                return self.map[x+1][y] == -1
            case move.LEFT:
                return self.map[x-1][y] == -1
            case move.UP:
                return self.map[x][y-1] == -1
            case move.DOWN:
                return self.map[x][y+1] == -1
            case _:
                return False

    def has_pellet(self, x: int, y: int):
        return self.map[x][y] == 1

    def eat_pellet(self, x: int, y: int):
        if self.map[x][y] == 1:
            self.map[x][y] = 0

    def get_tile(self, x: int, y: int):
        return self.map[x][y]