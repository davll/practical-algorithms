# https://www.hackerrank.com/challenges/qheap1/problem

import heapq

def heapify(h, i):
    n = len(h)
    while i in range(0, n):
        if i > 0: # not root
            p = (i+1) // 2 - 1 # parent
            if h[p] > h[i]:
                h[p], h[i] = h[i], h[p]
                i = p
                continue
        l = (i+1) * 2 - 1 # left child
        r = (i+1) * 2 # right child
        smallest = i
        if l < n and h[l] < h[smallest]:
            smallest = l
        if r < n and h[r] < h[smallest]:
            smallest = r
        if smallest != i:
            h[smallest], h[i] = h[i], h[smallest]
            i = smallest
        else:
            break

if __name__ == "__main__":
    h = []
    for _ in range(int(input().strip())):
        cmd = list(map(int, input().strip().split()))
        if cmd[0] == 1:
            i = len(h)
            h.append(cmd[1])
            heapify(h, i)
        elif cmd[0] == 2:
            k = -1
            for i in range(len(h)):
                if h[i] == cmd[1]:
                    k = i
                    break
            h[i], h[-1] = h[-1], h[i]
            h.pop()
            heapify(h, i)
        elif cmd[0] == 3:
            print(str(h[0]))
        else:
            raise RuntimeError()
