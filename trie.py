class Node(object):
    
    def __init__(self, data=None, children=None):
        self.data = data
        self.children = children

    def get_node_info(self):
        return "Current Node: " +self.data + " Children: " + self.children


class Trie(object):

    def __init__(self):
        self.root_of_trie = Node()
        self.immediate_child_node_keys = []

    def insert_into_trie(self, string_to_insert):

        if string_to_insert in self.immediate_child_node_keys:
            print("already in the trie")
        else:
            for letter in range(len(string_to_insert)):
                new_node = Node(string_to_insert[letter],string_to_insert[letter+1:len(string_to_insert)])
                self.immediate_child_node_keys.append(new_node)



        return ""

    def search(self):
        return ""


if __name__ == '__main__':
    x = "cat"
    y = "car"
    z = "house"

    trie = Trie()
    print(trie.insert_into_trie(x))

    keys = trie.immediate_child_node_keys
    for i in keys:
        print(i.get_node_info())
