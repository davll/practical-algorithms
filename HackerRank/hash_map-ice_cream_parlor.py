from sys import stdin, stdout, stderr

def whatFlavors(money, n, cost):
    c2i = {}
    for i, c in enumerate(cost):
        if c in c2i:
            c2i[c].append(i)
        else:
            c2i[c] = [i]
    if money % 2 == 0 and (money // 2) in c2i:
        a = c2i[money // 2]
        if len(a) >= 2:
            return a[:2]
    for i, c in enumerate(cost):
        if (money - c) in c2i:
            a = c2i[money-c]
            if a[0] != i:
                return list(sorted([i, a[0]]))
    return None

if __name__ == "__main__":
    for _ in range(int(stdin.readline().rstrip())):
        money = int(stdin.readline().rstrip())
        n = int(stdin.readline().rstrip())
        cost = list(map(int, stdin.readline().rstrip().split()))
        result = map(lambda x: x+1, whatFlavors(money, n, cost))
        stdout.write(' '.join(map(str, result)) + '\n')
