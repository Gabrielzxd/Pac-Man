import unittest

from src.Graph_utils import Graph, Node

class TestGraph_utils(unittest.TestCase):
    def setUp(self):
        self.graph = Graph()

    def test_add_Node(self):
        self.graph.addNode(1, 7, 18)
        self.assertIn(1, self.graph.nodes)
        self.assertEqual(self.graph.nodes[1].x, 7)
        self.assertEqual(self.graph.nodes[1].y, 18)

    def test_add_Node_without_parameters(self):
        self.graph.addNode(2)
        self.assertIn(2, self.graph.nodes)
        self.assertIsNone(self.graph.nodes[2].x)
        self.assertIsNone(self.graph.nodes[2].y)

    def test_add_Node_duplicate(self):
        self.graph.addNode(7)
        self.graph.addNode(7)
        self.assertEqual(len(self.graph.nodes), 1)

    # depois finalizar os testes

if __name__ == '__main__':
    unittest.main()
