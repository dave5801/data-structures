"""Class for testing BST."""
import random


def test_node_exists_no_args(tree_node):
    """Test Create a Tree Node."""
    assert tree_node


def test_if_iterable_is_inserted(bst):
    """Test for iterables."""
    from bst import Tree
    test_iter = [5, 3, 7]
    test_node = Tree(test_iter)
    assert test_node.root.data == test_iter[0]
    assert test_node.root.left.data == test_iter[1]
    assert test_node.root.right.data == test_iter[2]


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
    """Test no nodes has depth 0."""
    from bst import Tree
    test_tree = Tree()
    assert test_tree.get_depth() == 0


def test_get_depth_one_node():
    """Test one node has depth of one."""
    from bst import Tree
    test_tree = Tree()
    test_tree.insert(5)
    assert test_tree.get_depth(test_tree.root) == 1


def test_get_depth_small_tree():
    """Test multiple nodes has depth of 3."""
    from bst import Tree
    test_tree = Tree()
    test_tree.insert(5)
    test_tree.insert(2)
    test_tree.insert(3)
    test_tree.insert(1)
    test_tree.insert(7)

    assert test_tree.get_depth(test_tree.root) == 3


def test_is_root_balanced():
    """Test root is balanced."""
    from bst import Tree
    test_tree = Tree([5])
    assert test_tree.balanced() == 0


def test_two_nodes_balanced():
    """Test One root, and one left node."""
    from bst import Tree
    test_tree = Tree([5, 1])
    assert test_tree.balanced() == 1


def test_right_heavy_balanced_right():
    """Test tree is right heavy."""
    from bst import Tree
    test_tree = Tree([5, 1, 6, 7, 8])
    assert test_tree.balanced() == -1


def test_left_heavy_balanced_left():
    """Test tree is left heavy."""
    from bst import Tree
    test_tree = Tree([5, 4, 3, 2])
    assert test_tree.balanced() == 1


def test_larger_balanced_tree():
    """Test tree is balanced."""
    from bst import Tree
    test_tree = Tree([10, 5, 15, 4, 6, 11, 16])
    assert test_tree.balanced() == 0


def test_in_order_one():
    """Test sort one node."""
    from bst import Tree
    test_list = [10]

    test_tree = Tree(test_list)
    path = test_tree.in_order(test_tree.root)

    count = 0
    for i in path:
        assert i.data == test_list[count]
        count += 1


def test_in_order_multiple_nodes():
    """Test sort multiple nodes."""
    from bst import Tree
    test_list = [5, 2, 6, 1, 4]
    test_tree = Tree(test_list)
    path = test_tree.in_order(test_tree.root)

    test_results = [1, 2, 4, 5, 6]

    count = 0
    for i in path:
        assert i.data == test_results[count]
        count += 1


def test_pre_order_multiple_nodes():
    """Test preorder on larger tree."""
    from bst import Tree
    test_list = [10, 7, 12, 5, 9, 11, 13, 4]
    test_tree = Tree(test_list)

    test_results = [10, 7, 5, 4, 9, 12, 11, 13]

    path = test_tree.pre_order(test_tree.root)

    count = 0

    for i in path:
        assert i.data == test_results[count]
        count += 1


def test_post_order_multiple_nodes():
    """Test postorder on larger tree."""
    from bst import Tree
    test_list = [10, 7, 12, 5, 9, 11, 13, 4]
    test_tree = Tree(test_list)

    test_results = [7, 5, 4, 9, 12, 11, 13, 10]

    path = test_tree.post_order(test_tree.root)

    count = 0

    for i in path:
        assert i.data == test_results[count]
        count += 1


def test_breadth_first_traversal():
    """Test breadth_first traversal."""
    from bst import Tree
    test_list = [10, 7, 5, 9, 12, 11, 13]
    test_tree = Tree(test_list)

    x = test_tree.breadth_first()

    for i in x:
        assert i == [10, 7, 12, 5, 9, 11, 13]


def test_delete_root():
    """Test remove root."""
    from bst import Tree
    test_tree = Tree([10])
    test_tree.delete_node(10)
    assert test_tree.root is None


def test_delete_left_child():
    """Test remove left child."""
    from bst import Tree
    test_tree = Tree([10, 7])
    test_tree.delete_node(7)
    assert test_tree.root.left is None


def test_delete_right_child():
    """Test remove left child."""
    from bst import Tree
    test_tree = Tree([10, 7, 12])
    test_tree.delete_node(12)
    assert test_tree.root.right is None


def test_remove_right_child_larger_list():
    """Test remove right child from a larger list."""
    from bst import Tree
    test_tree = Tree([10, 7, 12, 15, 5])
    test_tree.delete_node(12)
    assert test_tree.root.right.data == 15


def test_remove_left_child_larger_list():
    """Test remove right child from a larger list."""
    from bst import Tree
    test_tree = Tree([10, 7, 12, 15, 5])
    test_tree.delete_node(7)
    assert test_tree.root.left.data == 5


def test_remove_root_larger_list():
    """Test remove root from larger list."""
    from bst import Tree
    test_tree = Tree([10, 7, 12, 15, 5])
    test_tree.delete_node(10)
    assert test_tree.root.data == 7
