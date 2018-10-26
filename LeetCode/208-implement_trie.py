class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node(None)
    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.root
        for c in word:
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
            if next_node:
                node = next_node
            else:
                # TODO: add new node
        # TODO: mark last node with end_of_word=True
    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self._find(word)
        return bool(node) and node.end_of_word
    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self._find(word)
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
        return str(self.key)

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
