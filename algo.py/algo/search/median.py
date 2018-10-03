# Median Heap for Running Median (Online Algorithm)

from typing import TypeVar, Generic, List
from algo.data.tree.heap import min_heap_push, max_heap_push, min_heap_pop, max_heap_pop, heap_peak

T = TypeVar('T', int, float)

class MedianHeap(Generic[T]):
    def __init__(self) -> None:
        self.left: List[T] = []
        self.right: List[T] = []
    #
    def query(self) -> float:
        nl, nr = len(self.left), len(self.right)
        if nl == 0 and nr == 0:
            raise IndexError()
        elif nl > nr:
            return heap_peak(self.left)
        elif nl < nr:
            return heap_peak(self.right)
        else: # nl == nr
            ml = heap_peak(self.left)
            mr = heap_peak(self.right)
            return (ml + mr) / 2
    #
    def insert(self, x: T) -> None:
        if not self.left and not self.right:
            max_heap_push(self.left, x)
        elif x <= heap_peak(self.left):
            max_heap_push(self.left, x)
            if len(self.left) > len(self.right) + 1:
                x = max_heap_pop(self.left)
                min_heap_push(self.right, x)
        elif not self.right or x >= heap_peak(self.right):
            min_heap_push(self.right, x)
            if len(self.left) + 1 < len(self.right):
                x = min_heap_pop(self.right)
                max_heap_push(self.left, x)
        elif len(self.left) < len(self.right):
            max_heap_push(self.left, x)
        else:
            min_heap_push(self.right, x)
        assert abs(len(self.left) - len(self.right)) <= 1

# https://www.geeksforgeeks.org/median-of-stream-of-integers-running-integers/
