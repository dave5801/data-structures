"""Class for Weighted Graph."""


class Vertex(object):
    """Class for Vertex creation."""

    def __init__(self, vertex=None):
        """Let vertex be: { "Node": {"N1" : i, "Nk" : ik} }."""
        self.node = None
        self.vertex = vertex
        self.neighbors = []

    def get_vertex(self):
        """Return primary node of a vertex."""
        return list(self.vertex.keys())[0]

    def update_neighbors(self):
        """Return all neighbors of a given vertex node."""

        for i in self.vertex:
            for j in self.vertex[i]:
                self.neighbors.append(j)

    def get_weight(self, neighbor):
        """Get weight from one neighbor."""

        weight = 0
        for i in self.vertex:
            weights = self.vertex[i]
            weight = weights[neighbor]

        return weight

    #add connection
    def add_connection(self, new_neighbor):
        self.neighbors.append(new_neighbor)


'''
class WGraph(object):
    def __init__ (self, vertices=None):
        self.vertices = []


    def return_vertices(self):
        for i in vertices:
            print(i)

    def add_vertex(self, vertex_to_add):
        """Add new vertex."""
        vertex = Vertex(vertex_to_add)
        self.vertices.append(vertex)
'''