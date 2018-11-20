class HashTable:
    def __init__(self, num_buckets = 32):
        self._buckets = [None] * num_buckets
        self._hash = hash
        self._count = 0
        self._load_factor = 0.75
    #
    def __contains__(self, key):
        code = self._hash(key)
        i = self._bucket_index(code)
        node = _ll_find(self._buckets[i], key, code)
        return bool(node)
    #
    def __setitem__(self, key, value):
        code = self._hash(key)
        i = self._bucket_index(code)
        node = _ll_find(self._buckets[i], key, code)
        if node:
            node.value = value
        else:
            node = Node(key, value, code)
            self._buckets[i] = _ll_push(self._buckets[i], node)
            self._count += 1
            if self._need_rehash():
                self._rehash(len(self._buckets) * 2)
    #
    def __getitem__(self, key, default=None):
        code = self._hash(key)
        i = self._bucket_index(code)
        node = _ll_find(self._buckets[i], key, code)
        if node:
            return node.value
        elif default is not None:
            return default
        else:
            raise IndexError()
    #
    def __delitem__(self, key):
        code = self._hash(key)
        i = self._bucket_index(code)
        node, self._buckets[i] = _ll_extract(self._buckets[i], key, code)
        if node:
            self._count -= 1
        else:
            raise IndexError()
    #
    def _bucket_index(self, code):
        return code % len(self._buckets)
    #
    def _rehash(self, num_buckets):
        buckets = [None] * num_buckets
        for old_bucket in self._buckets:
            while old_bucket:
                node, old_bucket = _ll_pop(old_bucket)
                i = node.code % num_buckets
                buckets[i] = _ll_push(buckets[i], node)
        self._buckets = buckets
    #
    def _need_rehash(self):
        return self._count / len(self._buckets) >= self._load_factor

class Node:
    def __init__(self, key, value, code):
        self.key = key
        self.value = value
        self.code = code
        self.next = None

# return root
def _ll_push(root, node):
    node.next = root
    return node

# return node
def _ll_find(root, key, code):
    while root:
        if root.code == code and root.key == key:
            break
        root = root.next
    return root

# return (node, root)
def _ll_extract(root, key, code):
    prev, curr = None, root
    while curr:
        if curr.code == code and curr.key == key:
            if prev:
                prev.next, curr.next = curr.next, None
            else:
                root, curr.next = curr.next, None
            return (curr, root)
        prev, curr = curr, curr.next
    return (None, root)

# return (node, root)
def _ll_pop(root):
    if not root:
        return (None, None)
    tmp, root.next = root.next, None
    return (root, tmp)

if __name__ == "__main__":
    from random import shuffle
    keys = list(range(1024))
    vals = list(map(lambda x: x**2, range(1,1024+1)))
    shuffle(keys)
    shuffle(vals)
    ht = HashTable()
    for k, v in zip(keys, vals):
        ht[k] = v
    for k, v in zip(keys, vals):
        assert k in ht
        assert v == ht[k]
        del ht[k]
