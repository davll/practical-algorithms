# Shell Sort
#
# Worst case: O(n^2) worst known gap seq., O(n*log(n)) best known gap seq.
# Avg case: depends on gap sequence
# Best case: O(n*log(n))
# Worst case space: O(1) aux
#

def shellsort(arr, gaps = None):
    n = len(arr)
    if not gaps:
        gaps = iter([701, 301, 132, 57, 23, 10, 4, 1])
    for g in gaps:
        # perform gapped insertion sort
        for i in range(g, n):
            # add arr[i] to the elements that have been gap sorted
            # save arr[i] in temp and make a hole at position i
            tmp = arr[i]
            # shift earlier gap-sorted elements up until the correct location for arr[i] is found
            j = i
            while j >= g and arr[j-g] > tmp:
                arr[j] = arr[j-g]
                j -= g
            # put temp (the original arr[i]) in its correct location
            arr[j] = tmp
