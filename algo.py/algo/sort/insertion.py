# Insertion Sort
#
# Worst case: O(n^2) comparisons, swaps
# Avg case: O(n^2) comparisons, swaps
# Best case: O(n) comparisons, O(1) swaps
# Worst case space: O(1) aux

from typing import TypeVar, MutableSequence

T = TypeVar('T', int, float)

def insertionsort(a: MutableSequence[T]) -> None:
    n = len(a)
    for i in range(1, n):
        for j in range(i, 0, -1):
            if a[j-1] > a[j]:
                a[j], a[j-1] = a[j-1], a[j]
            else:
                break
