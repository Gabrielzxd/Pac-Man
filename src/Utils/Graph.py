class Node:
    def __init__(self, id, x = None, y = None):
        self.id = id
        self.x = x
        self.y = y
        self.neighbors = []

class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, id, x = None, y = None):
        if id not in self.nodes:
            self.nodes[id] = Node(id, x, y)

    def add_edge(self, origin, destination):
        self.add_node(origin)
        self.add_node(destination)

        if destination not in self.nodes[origin].neighbors:
            self.nodes[origin].neighbors.append(destination)

        if origin not in self.nodes[destination].neighbors:
            self.nodes[destination].neighbors.append(origin)

    def get_edge(self, id):
        if id in self.nodes:
            return self.nodes[id].neighbors
        return []