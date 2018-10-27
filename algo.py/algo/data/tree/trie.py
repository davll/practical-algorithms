# Trie

class Trie:
    def __init__(self):
        self._root = Node(None)
    @property
    def root(self):
        return self._root
    #
    def insert(self, word):
        node = self.root
        for c in word:
            # search children
            l, r = 0, len(node.children)-1
            next_node = None
            pos = r+1
            while l <= r:
                m = (l+r)//2
                child = node.children[m]
                if child.char == c:
                    next_node = child
                    pos = m
                    break
                elif child.char < c:
                    l = m+1
                else:
                    r = m-1
                    pos = m
            if next_node:
                node = next_node
            else:
                next_node = Node(c)
                node.children.insert(pos, next_node)
                node = next_node
        node.end_of_word = True
    def has_word(self, word):
        node = self._find(word)
        return bool(node) and node.end_of_word
    def has_prefix(self, prefix):
        node = self._find(prefix)
        return bool(node)
    def _find(self, pattern):
        node = self.root
        for c in pattern:
            # search children
            l, r = 0, len(node.children)-1
            next_node = None
            while l <= r:
                m = (l+r)//2
                child = node.children[m]
                if child.char == c:
                    next_node = child
                    break
                elif child.char < c:
                    l = m+1
                else:
                    r = m-1
            node = next_node
            if not node:
                break
        return node
    

class Node:
    def __init__(self, char):
        self.char = char
        self.children = []
        self.end_of_word = False
    def __repr__(self):
        return "TrieNode({c})".format(c=self.char)
    def __str__(self):
        return str(self.char)
