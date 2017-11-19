"""Test class for Weighted Graph."""


def test_vertex_exists_no_args():
    """Test Graph Exists."""
    from weighted_graph import Vertex
    test_vertex = Vertex()
    assert test_vertex


def test_vertex_has_a_vertex_with_single_neighbor():
    """test vertex for single neighbor"""
    from weighted_graph import Vertex
    test_vertex = Vertex('A', ['B'], {'B': 5})
    test_data = 'A'
    test_neighbor = ['B']
    test_weight = {'B': 5}
    assert test_vertex.data == test_data
    assert test_vertex.neighbors == test_neighbor
    assert test_vertex.weights == test_weight


def test_vertex_multiple_neigbors():
    """test vertex multiple neighbors"""
    from weighted_graph import Vertex
    test_vertex = Vertex('A', ['B', 'C', 'D'], {'B': 5, 'C': 1, 'D': 3})
    test_data = 'A'
    test_neighbors = [['B', 'C', 'D']]
    test_wieghts = {'B': 5, 'C': 1, 'D': 3}
    assert test_vertex.data == test_data
    assert test_vertex.neighbors == test_neighbors
    assert test_vertex.weights == test_weights
