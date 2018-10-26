# Trie

from bisect import bisect_right
#from sys import stderr

class Trie:
    def __init__(self):
        self._root = Node(None, None, 0)
    @property
    def root(self):
        return self._root
    #
    def insert(self, s, value):
        node, depth = self.root, 1
        for c in s:
            # find a child with key = c
            i = bisect_right(node.children_keys, c)
            #print("c = %s, i = %d" % (c,i), file = stderr)
            if i > 0 and node.children_keys[i-1] == c:
                # found
                node = node.children[i-1]
                assert node.depth == depth
            else: # not found
                tmp = Node(c, None, depth)
                node.children.insert(i, tmp)
                node.children_keys.insert(i, c)
                node = tmp
            depth += 1
        node.end_of_word = True
        node.value = value
    #
    def _search(self, s):
        node = self.root
        for c in s:
            i = bisect_right(node.children_keys, c)
            # find a child with key = c
            i = bisect_right(node.children_keys, c)
            if node.children_keys[i-1] == c:
                # found
                node = node.children[i-1]
            else: # not found
                return None
        if node.end_of_word:
            return node
        else:
            return None
    #
    def __contains__(self, s):
        return self._search(s) is not None
    #
    def __getitem__(self, s):
        node = self._search(s)
        if node is None:
            raise IndexError()
        return node.value
    #
    def __setitem__(self, s, value):
        self.insert(s, value)
    #
    def items(self):
        def traverse(root, s):
            if root.key is not None:
                s.append(root.key)
            if root.end_of_word:
                yield ''.join(s)
            for child in root.children:
                yield from traverse(child, s)
            if root.key is not None:
                x = s.pop()
                assert x == root.key
        yield from traverse(self.root, [])

class Node:
    def __init__(self, key, value, depth):
        self.key = key
        self.value = value
        self.depth = depth
        self.children = []
        self.children_keys = []
        self.end_of_word = False
    def __repr__(self):
        return str(self.key)

if __name__ == "__main__":
    t = Trie()
    t['hello'] = 10
    t['hen'] = 100
    t['world'] = -10
    t['apple'] = 1984
    print("hello => %d" % t['hello'])
    print("hen => %d" % t['hen'])
    print("world => %d" % t['world'])
    print("apple => %d" % t['apple'])
    for x in t.items():
        print(x)
