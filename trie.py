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

        count = 1

        for current_node in self.immediate_child_node_keys:
            children = current_node.dictionary_of_child_nodes[current_node.data]
            print(children,  string_to_insert[count])
            if string_to_insert[count] in children:
                print("extend from here", string_to_insert[count])
            count += 1



        
        else:
            for letters in range(len(string_to_insert)):
                potential_children = string_to_insert[letters+1:len(string_to_insert)]
                if potential_children:
                    new_node = Node(string_to_insert[letters],potential_children[0])
                else:
                     new_node = Node(string_to_insert[letters])
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
