# Patience Sorting
#
# Worst case: O(n*log(n))
#

from functools import total_ordering
from bisect import bisect_left
from heapq import merge

@total_ordering
class Pile(list):
    def __lt__(self, other):
        return self[-1] < other[-1]
    def __eq__(self, other):
        return self[-1] == other[-1]

def patience_sort(arr):
    piles = []
    # sort into piles
    for x in arr:
        new_pile = Pile([x])
        # find the first index i such that piles[i][-1] >= x
        i = bisect_left(piles, new_pile)
        if i != len(piles):
            piles[i].append(x)
        else:
            piles.append(new_pile)
    # use heap-based merge to merge piles
    return list(merge(*[reversed(pile) for pile in piles]))

# References:
# https://en.wikipedia.org/wiki/Patience_sorting
# https://rosettacode.org/wiki/Sorting_algorithms/Patience_sort
# https://en.wikibooks.org/wiki/Algorithm_Implementation/Sorting/Patience_sort
