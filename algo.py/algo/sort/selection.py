# Selection Sort
#
# Worst case: O(n^2) comparisons, O(n) swaps
# Avg case: O(n^2) comparisons, O(n) swaps
# Best case: O(n^2) comparisons, O(n) swaps
# Worst case space: O(1) aux
#

from typing import TypeVar, MutableSequence

T = TypeVar('T', int, float)

def selectionsort(a: MutableSequence[T]) -> None:
    n = len(a)
    for i in range(n-1):
        j = min(range(i, n),  key=lambda j: a[j])
        if i != j:
            a[i], a[j] = a[j], a[i]
