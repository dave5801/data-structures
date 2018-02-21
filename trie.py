class Node(object):
    def __init__(self, data, children):
        self.data = data
        self.children = children


class Trie(object):

    def __init__(self):
        self.immediate_child_node_keys = []
        print("")
    

    def insert(self, string_to_insert):

        if string_to_insert in self.immediate_child_node_keys:
            print("already in the trie")
        else:
            self.immediate_child_node_keys.append(string_to_insert[0])

            for i in range(len(string_to_insert)):
                print(string_to_insert[i])



        return ""

    def search(self):
        return ""


if __name__ == '__main__':
    x = "cat"
    y = "car"
    z = "house"

    trie = Trie()
    print(trie.insert(x))
