class Node:
    def __init__(self, id, x = None, y = None):
        self.id = id
        self.x = x
        self.y = y
        self.neighbors = []

class Graph:
    def __init__(self):
        self.nodes = {}

    def addNode(self, id, x = None, y = None):
        if id not in self.nodes:
            self.nodes[id] = Node(id, x, y)

    def addEdge(self, origin, destination):
        self.addNode(origin)
        self.addNode(destination)

        if destination not in self.nodes[origin].neighbors:
            self.nodes[origin].neighbors.append(destination)

        if origin not in self.nodes[destination].neighbors:
            self.nodes[destination].neighbors.append(origin)

    def getEdge(self, id):
        if id in self.nodes:
            return self.nodes[id].neighbors
        return []