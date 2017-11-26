import pytest

@pytest.fixture
def tree_node():
    from bst import TreeNode
    return TreeNode()

@pytest.fixture
def bst():
    from bst import Tree
    return Tree()