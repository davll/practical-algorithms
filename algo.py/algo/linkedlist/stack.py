from . import Node

class Stack:
    def __init__(self):
        self._top = None
        self._btm = None
    @property
    def top(self):
        if not self._top:
            raise IndexError()
        return self._top.value
    @property
    def bottom(self):
        if not self._btm:
            raise IndexError()
        return self._btm.value
    #
    def push(self, val):
        self._top = Node(val, self._top)
        if not self._btm:
            self._btm = self._top
    def pop(self):
        v = self._top.value
        n = self._top.next
        self._top = n
        if not n:
            self._btm = None
        return v
    def merge(self, stack):
        if not self._btm:
            self._top = stack._top
            self._btm = stack._btm
        else:
            self._btm.next = stack._top
            self._btm = stack.btm
