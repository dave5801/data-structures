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

    def contains(self, val):
        """Search for value in BST."""
        if val in self.nodes:
            return True
        else:
            return False

    def insert(self, val):
        """Insert New Node."""
        if self.contains(val) == True:
            """Ignore if already present."""
            return

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

    def search(self, val):
        """Search method."""
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

    def balanced(self):
        """Check Balance of Tree."""
        if self.size() <= 1:
            return 0

        if self.root.left and not self.root.right:
            """Return 1, if balance is left."""
            return 1
        elif self.root.right and not self.root.left:
            """Return -1, if balance is right."""
            return -1

        lh = self.get_depth(self.root.left)
        rh = self.get_depth(self.root.right)

        """Return 0 if balance."""
        if lh == rh:
            return 0
        elif lh > rh:
            return 1
        else:
            return -1

    def get_depth(self, node=None):
        """Get depth of tree."""
        if node is None:
            return 0

        if node.left and not node.right:
            return self.get_depth(node.left) + 1
        elif node.right and not node.left:
            return self.get_depth(node.right) + 1
        else:
            return max(self.get_depth(node.left), self.get_depth(node.right)) + 1

    def in_order(self, node=None):
        """Search in ascending order."""
        if node is None:
            return
        if node.left:
            for i in self.in_order(node.left):
                yield i
        yield node
        if node.right:
            for i in self.in_order(node.right):
                yield i

    def pre_order(self, node=None):
        """Search in descending order."""
        if node is None:
            return

        yield node

        if node.left:
            for i in self.pre_order(node.left):
                yield i
        if node.right:
            for i in self.pre_order(node.right):
                yield i

    def post_order(self, node=None):
        """Search lowest children first."""
        if node is None:
            return

        if node.left:
            for i in self.pre_order(node.left):
                yield i
        if node.right:
            for i in self.pre_order(node.right):
                yield i

        yield node

    def breadth_first(self):
        """Search by breadth first."""
        s = [self.root]

        res = []

        while s:
            if s[0].left:
                s.append(s[0].left)

            if s[0].right:
                s.append(s[0].right)

            res.append(s.pop(0).data)

        yield res

    def delete_node(self, val):
        """Delete node from BST."""
        if self.root is None:
            return None
        else:
            self.delete(val, self.root)
    
    def delete(self, val, node):
        if node.data == val:
            print("Found node for deletion")
            return
        

        '''
    def delete_node(self, node):
        """delete node from tree."""
        if self.root is None:
            return
        elif node == self.root:

            if self.root.right is None:
                print("trying to get left child")
                self.root = self.root.left
                self.left = None

            self.root = self.get_min_node(node)'''

        '''
             
        if node.data < self.root.data:
            print("Traverse here",self.root.left.data)
            self.root.left = self.delete_node(self.root)
           
        elif node.data > self.root.data:
            print("Traverse here",self.root.right.data)
       '''

        
     

    def get_min_node(self, node):
        """get min node from sub tree."""
        if node.left:
            return node.left
        else:
            return node.right

if __name__ == '__main__':

   # t = Tree([10, 7, 12, 5, 9, 11, 13])
   # t = Tree([5,3,1,6])
    t = Tree([])

    t.delete_node(10)
   # print(t.root.right)
   # t.delete_node(t.root)
   # print(t.root.data)
   # print(t.root.left)




