class Node(object):
    
    def __init__(self, data=None, children=None):
        self.data = data
        self.children = children


class Trie(object):

    def __init__(self):
        self.root_of_trie = Node()
        self.immediate_child_node_keys = []

    def insert_into_trie(self, string_to_insert):

        if string_to_insert in self.immediate_child_node_keys:
            print("already in the trie")
        else:
            self.immediate_child_node_keys.append(string_to_insert[0])

            for letter in range(len(string_to_insert)):
                print(string_to_insert[letter])



        return ""

    def search(self):
        return ""


if __name__ == '__main__':
    x = "cat"
    y = "car"
    z = "house"

    trie = Trie()
    print(trie.insert_into_trie(x))
