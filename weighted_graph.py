"""Class for Weighted Graph."""


class Vertex(object):
    """Vertex component of a graph."""
    def __init__ (self, data=None, neighbors=None, weights=None):
        self.data = data
        self.neighbors = neighbors
        self.weights = weights
