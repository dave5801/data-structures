"""Class for Binary Search Tree."""

import collections

class TreeNode(object):
    """Class for For Node of Tree."""

    def __init__(self, data=None, left=None, right=None):
        """Constructor."""
        self.data = data
        self.left = left
        self.right = right


class Tree(object):
    """Tree Class."""

    def __init__(self, iterable=None):
        """Constructor."""
        self.root = None
        self.nodes = []

        if isinstance(iterable, collections.Iterable):
            for i in iterable:
                self.insert(i)

    def size(self):
        """Return size of Tree."""
        if not self.nodes:
            return 0
        else:
            return len(self.nodes)

    def insert(self, val):
        """Insert New Node."""

        if self.root is None:
            self.root = TreeNode(val)
            self.nodes.append(val)
            return

        current = self.root

        while current:
            if val < current.data:
                if current.left:
                    current = current.left
                else:
                    current.left = TreeNode(val)
                    self.nodes.append(val)
                    break
            if val > current.data:
                if current.right:
                    current = current.right
                else:
                    current.right = TreeNode(val)
                    self.nodes.append(val)
                    break
                '''
                '''
    def contains(self, val):
        """Search for value in BST"""
        if val in self.nodes:
            return True
        else:
            return False

    def search(self, val):
     
        if self.root is None:
            return

        current = self.root

        while current:

            if current.data == val:
                return current

            if val < current.data:
                current = current.left
            elif val > current.data:
                current = current.right

        return None
        

    def get_depth(self, node=None):
        """Get depth of tree"""

        if node is None:
            return 0

        ld = self.get_depth(node.left)
        rd = self.get_depth(node.right)

        if node.left and node.left.data > node.right.data:
            return ld + 1
        else:
            return rd + 1


if __name__ == '__main__':
    t = Tree([5,6, 7])
    #t.insert(5)
    #t.insert(2)
    #t.insert(3)
    #t.insert(1)
    #t.insert(7)
    #t.insert(10)
    #t.insert(20)
    #t.insert(30)

    print(t.root.right.right.data)
    #print(t.nodes)
   # print(t.size())
   # print(t.get_depth(t.root))

    
