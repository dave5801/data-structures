"""Class for Binary Search Tree."""


class TreeNode(object):
    """Class for For Node of Tree."""

    def __init__(self, data=None, left=None, right=None):
        """Constructor."""
        self.data = data
        self.left = left
        self.right = right


class Tree(object):
    """Tree Class."""

    def __init__(self):
        """Constructor."""
        self.root = None
        self.nodes = []

    def size(self):
        """Return size of Tree."""
        return self.size

    def insert(self, val):
        """Insert New Node."""

        if self.root is None:
            self.root = TreeNode(val)
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
    t = Tree()
    t.insert(5)
    t.insert(2)
    t.insert(3)
    t.insert(1)
    t.insert(7)
    t.insert(10)
    t.insert(20)
    t.insert(30)

    #print(t.search(5).data)
    print(t.get_depth(t.root))
    
