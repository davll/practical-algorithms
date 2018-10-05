# https://www.hackerrank.com/challenges/minimum-time-required/problem

from sys import stdin, stdout, stderr

def items_for_days(machines, days):
    return sum(map(lambda x: (days // x), machines))

def minimumTime(machines, goal):
    machines.sort()
    l = (goal * machines[0]) // len(machines)
    r = (goal * machines[-1] + len(machines)-1) // len(machines)
    while l < r:
        m = (l + r) // 2
        nitems = items_for_days(machines, m)
        if nitems < goal:
            l, r = m+1, r
        elif nitems > goal:
            l, r = l, m-1
        else: # nitems == goal
            r = m
    while items_for_days(machines, r) < goal:
        r = r + 1
    return r

if __name__ == "__main__":
    n, goal = map(int, stdin.readline().rstrip().split())
    machines = list(map(int, stdin.readline().rstrip().split()))
    assert len(machines) == n
    ans = minimumTime(machines, goal)
    stdout.write(str(ans) + '\n')
