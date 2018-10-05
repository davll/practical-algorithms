# https://www.hackerrank.com/challenges/triple-sum/problem

from sys import stdin, stdout, stderr

def triplets(la, lb, lc):
    la.sort()
    lb.sort()
    lc.sort()
    na, nb, nc = len(la), len(lb), len(lc)
    ia, ic, cnt, ca, cc = 0, 0, 0, 0, 0
    for ib, q in enumerate(lb):
        if ib > 0 and lb[ib] == lb[ib-1]:
            continue
        while ia < na and la[ia] <= q:
            if ia == 0 or la[ia] != la[ia-1]:
                ca += 1
            ia += 1
        while ic < nc and lc[ic] <= q:
            if ic == 0 or lc[ic] != lc[ic-1]:
                cc += 1
            ic += 1
        cnt += ca * cc
    return cnt

if __name__ == "__main__":
    na, nb, nc = map(int, stdin.readline().rstrip().split())
    la = list(map(int, stdin.readline().rstrip().split()))
    lb = list(map(int, stdin.readline().rstrip().split()))
    lc = list(map(int, stdin.readline().rstrip().split()))
    assert len(la) == na
    assert len(lb) == nb
    assert len(lc) == nc
    ans = triplets(la, lb, lc)
    stdout.write(str(ans) + '\n')
