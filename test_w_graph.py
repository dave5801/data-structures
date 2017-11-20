"""Test class for Weighted Graph."""


def test_vertex_exists_no_args():
    """Test Graph Exists."""
    from weighted_graph import Vertex
    test_vertex = Vertex()
    assert test_vertex


def test_vertex_has_single_neighbor():
    """Test creation of new vertex."""
    from weighted_graph import Vertex
    test_vertex = Vertex({'A': {'B': 5}})

    assert test_vertex.get_vertex() == 'A'
    test_vertex.update_neighbors()

    assert test_vertex.neighbors == ['B']


def test_vertex_get_weight_from_single_neighbor():
    """Test getting a single weight."""
    from weighted_graph import Vertex
    test_vertex = Vertex({'A': {'B': 5}})

    test_vertex.update_neighbors()

    test_neighbor_list = test_vertex.neighbors
    test_neighbor = test_neighbor_list[0]

    assert test_vertex.get_weight(test_neighbor) == 5


def test_vertex_has_multiple_neighbors():
    """Test if Vertex has multiple neighbors."""
    from weighted_graph import Vertex
    test_vertex = Vertex({'A': {'B': 5, 'C': 10, 'D': 6}})
    test_vertex.update_neighbors()

    assert test_vertex.neighbors == ['B', 'C', 'D']


def test_vertex_get_weight_one_of_many_neighbors():
    """Test if single weight returned from multi neighbors."""
    from weighted_graph import Vertex

    test_vertex = Vertex({'A': {'B': 5, 'C': 10, 'D': 6}})
    test_vertex.update_neighbors()

    test_neighbor_list = test_vertex.neighbors
    test_neighbor = test_neighbor_list[1]
    assert test_vertex.get_weight(test_neighbor) == 10


'''
def test_vertex_has_a_vertex_with_single_neighbor():
    """test vertex for single neighbor."""
    from weighted_graph import Vertex
    test_vertex = Vertex('A', ['B'], {'B': 5})
    test_data = 'A'
    test_neighbor = ['B']
    test_weight = {'B': 5}
    assert test_vertex.data == test_data
    assert test_vertex.neighbors == test_neighbor
    assert test_vertex.weights == test_weight


def test_vertex_multiple_neigbors():
    """test vertex multiple neighbors."""
    from weighted_graph import Vertex
    test_vertex = Vertex('A', ['B', 'C', 'D'], {'B': 5, 'C': 1, 'D': 3})
    test_data = 'A'
    test_neighbors = ['B', 'C', 'D']
    test_weights = {'B': 5, 'C': 1, 'D': 3}
    assert test_vertex.data == test_data
    assert test_vertex.neighbors == test_neighbors
    assert test_vertex.weights == test_weights

def test_wieghted_graph_exists():
    """Test if graph is created."""
    from weighted_graph import WGraph
    wgraph = WGraph()
    assert wgraph


def test_weighted_graph_add_one_vertex():
    from weighted_graph import WGraph
    wgraph = WGraph()
    wgraph.add_vertex()
'''
