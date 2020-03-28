# Binomial Heap

class BinomialHeap:
    """
    Binomial Heap
    """
    def __init__(self):
        self.forest = []
    #
    # T = O(log(n))
    def peak(self):
        # find a tree with the smallest root
        return min(map(lambda t: t.key, filter(bool, self.forest)), default=None)
    #
    # T = O(1) amortized
    def push(self, key):
        # add a 0-order tree to the forest
        forest_append(self.forest, Node(key))
    #
    # T = O(log(n)) amortized
    def pop(self):
        # find a tree with the smallest root
        tree = min(filter(bool, self.forest), key=lambda t: t.key, default=None)
        if not tree:
            raise ValueError("The heap is empty")
        # remove the tree from the forest
        self.forest[tree.order] = None
        # move its children to the forest
        for t in tree.drain_children():
            forest_append(self.forest, t)
        # return the key of the root
        return tree.key
    #
    # T = O(log(n))
    def merge(self, other):
        # move all the trees to my forest
        for t in filter(bool, other.forest):
            forest_append(self.forest, t)
        # clear the input forest
        other.forest.clear()
    #
    # T = O(log(n))
    def empty(self):
        return not any(map(bool, self.forest))
    #
    def __bool__(self):
        return not self.empty()
    #
    # Generate Graphviz Plot
    def graphviz(self):
        from graphviz import Digraph
        g = Digraph(node_attr={})
        g.attr('node', shape='circle', width='0.9')
        plot_forest(g, self.forest)
        return g

# Tree node
class Node:
    def __init__(self, key):
        self.key = key
        self.next = None
        self.children_head = None
        self.children_tail = None
        self.order = 0
    #
    def join_tree(self, tree):
        """
        Join the tree
        """
        assert not tree.next
        assert self.order == tree.order
        if self.children_head:
            assert not self.children_tail.next
            self.children_tail.next = tree
        else:
            self.children_head = tree
        self.children_tail = tree
        self.order += 1
    #
    def drain_children(self):
        child = self.children_head
        self.children_head = None
        self.children_tail = None
        while child:
            tmp = child.next
            child.next = None
            yield child
            child = tmp
    #
    def children(self):
        child = self.children_head
        while child:
            yield child
            child = child.next

def forest_append(forest, tree):
    assert not tree.next
    while tree.order < len(forest) and forest[tree.order]:
        a, b = forest[tree.order], tree
        forest[tree.order] = None
        if a.key > b.key:
            a, b = b, a
        a.join_tree(b)
        tree = a
    if tree.order == len(forest):
        forest.append(tree)
    elif tree.order < len(forest):
        assert forest[tree.order] is None
        forest[tree.order] = tree
    else:
        raise RuntimeError("unexpected")

def plot_tree(graph, tree, column, node_graph):
    from graphviz import nohtml
    # plot the node
    tname = 'node-{}'.format(id(tree))
    node_graph.node(tname, nohtml(str(tree.key)), group='g-{}'.format(column))
    # plot subtrees
    for c in tree.children():
        cname, column = plot_tree(graph, c, column, graph)
        graph.edge(tname, cname)
        column += 1
    return tname, column

def plot_forest(graph, forest):
    col = 0
    with graph.subgraph() as s:
        s.attr(rank='same')
        s.node('root', '', shape='diamond', width='0.2', height='0.2')
        prev = 'root'
        for t in filter(bool, forest):
            curr, col = plot_tree(graph, t, col, s)
            s.edge(prev, curr, style='dashed', dir='none')
            col += 1
            prev = curr

if __name__ == "__main__":
    h = BinomialHeap()
    for x in [5, 2, 10, 3, 1, 6, 8, 12, 100, 4]:
        h.push(x)
        g = h.graphviz()
        g.attr(label="Added {}".format(x))
        g.view()
        input("Press Enter to continue")
    popped = []
    while h:
        x = h.pop()
        popped.append(x)
        g = h.graphviz()
        g.attr(label="Popped: [{}]".format(', '.join(map(str,popped))))
        g.view()
        input("Press Enter to continue")
