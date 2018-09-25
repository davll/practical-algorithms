

if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        c = list(map(int, input().strip().split()))
        edges = []
        for _ in range(n-1):
            edges.append(tuple(map(int, input().strip().split())))
        result = balanced_forest(c, edges)
        print(str(result))
