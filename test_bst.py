"""Class for testing BST"""
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
    assert test_tree.size == 0


def test_insert_one_node_return_size_one():
    from bst import Tree
    test_tree = Tree()
    test_tree.insert(1)
    assert test_tree.size == 1

'''
def test_insert_three_nodes_return_size():
    from bst import Tree
    test_tree = Tree()
    test_values = random.sample(range(100), 10)
    for i in test_values:
        test_tree.insert(i)

    assert test_tree.size == len(test_values)
    '''