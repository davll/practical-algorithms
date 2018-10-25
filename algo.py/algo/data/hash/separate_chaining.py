class Entry():
    def __init__(self, key, hash, value):
        self.key = key
        self.hash = hash
        self.value = value
        self.next = None
    def match(self, key, hash) -> bool:
        return self.hash == hash and self.key == key

class HashTable:
    def __init__(self, hash=hash) -> None:
        self._head = [None] * 64
        self._hash = hash
        self._load_factor = 0.75
        self._count = 0
    #
    def __contains__(self, key) -> bool:
        return bool(self._find(key))
    #
    def get(self, key, default=None):
        h = self._hash(key)
        i = h % len(self._head)
        #
        node = self._head[i]
        while node and not node.match(key, h):
            node = node.next
        #
        if node:
            return node.value
        elif default:
            return default
        else:
            raise IndexError()
    #
    def insert(self, key, value) -> None:
        h = self._hash(key)
        i = h % len(self._head)
        #
        node = self._head[i]
        while node and not node.match(key, h):
            node = node.next
        #
        if node:
            node.value = value
        else:
            node = Entry(key, h, value)
            node.next = self._head[i]
            self._head[i] = node
            self._count += 1
            if self._count / len(self._head) >= self._load_factor:
                self._rehash()
    #
    def remove(self, key) -> None:
        h = self._hash(key)
        i = h % len(self._head)
        #
        node = self._head[i]
        if not node:
            raise IndexError()
        elif node.match(key, h):
            self._head[i] = node.next
            self._count -= 1
        else:
            while node.next:
                if node.next.match(key, h):
                    node.next = node.next.next
                    self._count -= 1
                    return
                else:
                    node = node.next
            raise IndexError()
    #
    def _rehash(self) -> None:
        n = 2 * len(self._head)
        new_head = [None] * n
        for j, head in enumerate(self._head):
            if not head:
                continue
            # extract node
            node, self._head[j] = head, head.next
            node.next = None
            # add to new table
            h = node.hash
            i = h % n
            node.next = new_head[i]
            new_head[i] = node
        self._head = new_head

if __name__ == "__main__":
    import random
    keys = list(range(128))
    vals = list(map(lambda x: x**2, range(1,129)))
    random.shuffle(keys)
    random.shuffle(vals)
    ht = HashTable()
    for k, v in zip(keys, vals):
        ht.insert(k, v)
    for k, v in zip(keys, vals):
        assert v == ht.get(k)
