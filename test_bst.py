"""Class for testing BST."""
import random


def test_node_exists_no_args():
    """Test Create a Tree Node."""

    from bst import TreeNode

    test_node = TreeNode()

    assert test_node


def test_node_exists_args():
    """Test Create a Tree Node."""

    from bst import TreeNode

    test_node = TreeNode(1, 2, 3)

    assert test_node


def test_create_tree_none_root():
    """Test create an empty tree."""
    from bst import Tree
    test_tree = Tree()
    assert test_tree.size() == 0


def test_insert_one_node_return_size_one():
    """Test for one node insertion."""
    from bst import Tree
    test_tree = Tree()
    test_tree.insert(1)
    assert test_tree.size() == 1


def test_insert_mulitple_nodes_return_correct_size():
    """Test for multiple node insertion."""
    from bst import Tree
    test_tree = Tree()
    test_values = random.sample(range(100), 10)
    for i in test_values:
        test_tree.insert(i)

    assert test_tree.size() == len(test_values)


def test_search_one_node():
    """Test search for one node from inserted list of nodes."""
    from bst import Tree
    test_tree = Tree()
    test_node_list = [1, 2, 3, 4, 5]

    for i in test_node_list:
        test_tree.insert(i)

    assert test_tree.search(test_node_list[2]).data == 3


def test_search_mulitple_nodes():
    """Test multiple node searches."""
    from bst import Tree
    test_tree = Tree()
    test_values = random.sample(range(100), 10)
    for i in test_values:
        test_tree.insert(i)

    for j in test_values:
        assert test_tree.search(j).data == j


def test_get_depth_no_nodes():
    """Test no nodes has depth 0"""
    from bst import Tree
    test_tree = Tree()
    assert test_tree.get_depth() == 0


def test_get_depth_one_node():
    """Test one node has depth of one"""
    from bst import Tree
    test_tree = Tree()
    test_tree.insert(5)
    assert test_tree.get_depth(test_tree.root) == 1

def get_depth_small_tree():
    """Test multiple nodes has depth of 3."""
    from bst import Tree
    test_tree = Tree()
    test_tree.insert(5)
    test_tree.insert(2)
    test_tree.insert(3)
    test_tree.insert(1)
    test_tree.insert(7)

    assert test_tree.get_depth(test_tree.root) == 3



