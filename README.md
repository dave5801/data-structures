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



# Javascript

    # Singly Linked List

        # push() - add new node to list, O(1)

        # pop() - remove head of list, O(1)

        # get_size() - returns size of list, O(1) - this.size keeps track of add/removes.

        # search() - returns node which matches target value, O(n), must search through list elements.

    #DLL - Doubly Linked List

        #len() - returns size of list, O(1)

        #push() - add new node to list, O(1)

        #append() - add new node to end of list, O(1)

        #pop() - remove head of list, O(1)

        #shift() - returns and removes tail of list, O(1)

        #remove() - search through and remove value from list, adjusting list contents, O(n)

    #Stack

        #Methods implemented using a Singly linked list, size(), push(), pop(), len()

    #Testing - all testing is accomplished using Jest - https://facebook.github.io/jest/

# remove() - remove target node; resetting pointers, O(1) 

# display() - display list contents O(n), prints list contents in linear fashion.