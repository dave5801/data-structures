class Node(object):

    def __init__(self, data=None, children=None):
        self.dictionary_of_child_nodes = {}
        self.data = data
        self.children = [children]
        self.dictionary_of_child_nodes[data] = self.children


class Trie(object):

    def __init__(self):
        self.root_of_trie = Node()
        self.immediate_child_node_keys = []

    def insert_into_trie(self, string_to_insert):

        for current_node in self.immediate_child_node_keys:
            print("child nodes ",current_node.data, current_node.dictionary_of_child_nodes)


        if string_to_insert[0] in self.immediate_child_node_keys:
            print("already in the trie")
        else:
            for letter in range(len(string_to_insert)):
                #string slice, then split to list, then add to dict
                potential_children = string_to_insert[letter+1:len(string_to_insert)]
                if potential_children:
                    print("potential_children",potential_children[0])
                    new_node = Node(string_to_insert[letter],potential_children[0])
                else:
                     new_node = Node(string_to_insert[letter])
                self.immediate_child_node_keys.append(new_node)



        return ""

    def search(self):
        return ""


if __name__ == '__main__':
    x = "cat"
    y = "car"
    z = "house"

    print("Create New Node")
    node = Node("c", ["a", "t"])
    print(node.dictionary_of_child_nodes)
    print()

    trie = Trie()
    print("Create new Trie and Insert")
    print(trie.insert_into_trie(x))

    keys = trie.immediate_child_node_keys


    print("Second Test Case")    
    print(trie.insert_into_trie(y))    
