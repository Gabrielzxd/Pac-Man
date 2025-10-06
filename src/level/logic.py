from src.utils.graph import Graph
from move import *

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

    def create_graph(self):
        graph = Graph()
        for i in range(self.Row):
            for j in range(self.Col):
                if self.map[i][j] == 1 or self.map[i][j] == 0:
                    graph.add_node((i, j), i, j)
                    if i + 1 < self.Row and (self.map[i+1][j] == 1 or self.map[i+1][j] == 0):
                        graph.add_edge((i, j), (i + 1, j))
                    if i - 1 >= 0 and (self.map[i-1][j] == 1 or self.map[i-1][j] == 0):
                        graph.add_edge((i, j), (i - 1, j))
                    if j + 1 < self.Col and (self.map[i][j+1] == 1 or self.map[i][j+1] == 0):
                        graph.add_edge((i, j), (i, j + 1))
                    if j - 1 >= 0 and (self.map[i][j-1] == 1 or self.map[i][j-1] == 0):
                        graph.add_edge((i, j), (i, j - 1))
        return graph

    def is_wall(self, move: Move, x: int, y: int) -> bool:
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

    def has_pellot(self, x: int, y: int) -> bool:
        return self.map[x][y] == 1

    def eat_pellot(self, x: int, y: int):
        if self.map[x][y] == 1:
            self.map[x][y] = 0

    def get_tile(self, x: int, y: int) -> int:
        return self.map[x][y]