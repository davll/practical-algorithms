# https://www.hackerrank.com/challenges/poisonous-plants/problem

from sys import stdin, stdout, stderr

def poisonousPlants_Naive(p):
    q = []
    days = 0
    while True:
        cont = False
        q.clear()
        q.append(p[0])
        for i in range(1, len(p)):
            if p[i-1] >= p[i]:
                q.append(p[i])
            else:
                cont = True
        p, q = q, p
        if not cont:
            break
        days += 1
    return days

def poisonousPlants(p):
    # Initialize stacks
    stacks = [Stack()]
    stacks[0].push(p[-1])
    for i in range(len(p)-2, -1, -1):
        if p[i] >= stacks[-1].top.val:
            stacks[-1].push(p[i])
        else:
            s = Stack()
            s.push(p[i])
            stacks.append(s)
    stacks.reverse()
    #stderr.write(str(stacks) + '\n')
    days = 0
    while len(stacks) > 1:
        # make progress
        stacks2 = stacks[:1]
        for i in range(1, len(stacks)):
            if stacks[i-1].btm.val >= stacks[i].top.val:
                # keep
                stacks2.append(stacks[i])
            else:
                # pop one value
                _, s = pop(stacks[i])
                stacks2.append(s)
        # merge stacks
        stacks.clear()
        stacks.append(stacks2[0])
        for i in range(1, len(stacks2)):
            if not stacks2[i].top:
                continue
            if stacks[-1].btm.val >= stacks2[i].top.val:
                stacks[-1] = merge(stacks[-1], stacks2[i])
            else:
                stacks.append(stacks2[i])
        # accum day
        days += 1
    return days

class Stack:
    def __init__(self):
        self.top = None
        self.btm = None
    def push(self, val):
        self.top = Node(val, self.top)
        if not self.btm:
            self.btm = self.top
    def items(self):
        n = self.top
        while n:
            yield n.val
            n = n.next
    def __repr__(self):
        return '[' + ', '.join(map(str, self.items())) + ']'

def pop(stack):
    s = Stack()
    s.top = stack.top.next
    s.btm = stack.btm if stack.top.next else None
    return (stack.top.val, s)

def merge(stk1, stk2):
    s = Stack()
    stk1.btm.next = stk2.top
    s.top = stk1.top
    s.btm = stk2.btm
    return s

class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

if __name__ == "__main__":
    n = int(stdin.readline().rstrip())
    p = list(map(int, stdin.readline().rstrip().split()))
    ans = poisonousPlants(p)
    stdout.write(str(ans) + '\n')
