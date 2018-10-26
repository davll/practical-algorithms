# https://www.hackerrank.com/challenges/minimum-time-required/problem

from sys import stdin, stdout, stderr

# O(n)
def items_for_days(machines, days):
    return sum(map(lambda x: (days // x), machines))

def minimumTime(machines, goal):
    machines.sort()
    l = (goal * machines[0]) // len(machines)
    r = (goal * machines[-1] + len(machines)-1) // len(machines)
    ans = -1
    # O( n * log(goal * max(machine) / n) )
    while l <= r:
        m = (l + r) // 2
        #stderr.write("L = {l}, R = {r}, M = {m}\n".format(l=l, r=r, m=m))
        # O(n)
        nitems = items_for_days(machines, m)
        if nitems < goal:
            #stderr.write("X = {x} < GOAL = {g}\n".format(x=nitems, g=goal))
            l = m+1
        elif nitems > goal:
            #stderr.write("X = {x} > GOAL = {g}\n".format(x=nitems, g=goal))
            ans = m
            r = m-1
        else: # nitems == goal
            #stderr.write("X = {x} = GOAL = {g}\n".format(x=nitems, g=goal))
            ans = m
            r = m-1
    #while items_for_days(machines, r) < goal:
    #    r = r + 1
    return ans

if __name__ == "__main__":
    n, goal = map(int, stdin.readline().rstrip().split())
    machines = list(map(int, stdin.readline().rstrip().split()))
    assert len(machines) == n
    ans = minimumTime(machines, goal)
    stdout.write(str(ans) + '\n')
