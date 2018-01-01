# data-structures

# Binary Search Tree

    #This data structure has the property where left child node must be less than its parent,
    while its right child is greater. 

    #Since this informations is already organized time complexity will be O(logn)

    # insert - add new Tree Node to BST. 

    # search - Search left and rode nodes for matching values.

    # get_depth - recursively get depth of left and right nodes.

    # contains - returns true if node is in list

    # balance - return -1 if the tree is right heavy, 1 if it is left heavy, and 0 if the tree is balanced.

    # in_order : recursively sort in ascending order, O(n)

    # pre_order : recursively sort in descending order, O(n)

    # post_order: sort by subtrees recursively back up to root, O(n)

    # breadth first: also known as level order, search by left and right nodes in descending order, O(n)

    # delete_node: checks if the root is none, or the root is to be deleted, else pass to delete helper

    # delete: proper node deletion from BST, O(log n) relative to the height of the tree, assumming its balanced

# extra-credit

# Valid Parenthesis - https://www.codewars.com/kata/valid-parentheses/train/python

    # Utilizes stack
    # For every element popped from stack, use counter to check if balanced
    # if element equals '(' add 1, if ')' subtract one
    # use the count to validate if parenthesis is valid