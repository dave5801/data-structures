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
        self.size = 0
        self.root = None

    def size(self):
        """Return size of Tree."""
        return self.size

    def insert(self, val):
        """Insert New Node."""

        if self.root is None:
            self.root = TreeNode(val)
            self.size += 1
            return

        current = self.root

        while current:
            if val < current.data:
                if current.left:
                    current = current.left
                else:
                    current.left = TreeNode(val)
                    self.size += 1
                    break
            if val > current.data:
                if current.right:
                    current = current.right
                else:
                    current.right = TreeNode(val)
                    self.size += 1
                    break

    def search(self, val):
        
        if self.root is None:
            return

        current = self.root

        while current:

            if val < current.data:
                if current.left:
                    current = current.left
            elif val > current.data:
                if current.right:
                    current = current.right
            elif current.data == val:
                return current.data
            else:
                return None
           


if __name__ == '__main__':
    t = Tree()
    t.insert(10)
    t.insert(5)
    t.insert(8)
    print(t.search(8))
