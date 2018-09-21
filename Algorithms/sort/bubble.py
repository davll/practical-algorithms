# T = O(n^2)
def bubblesort(a):
    n = len(a)
    for _ in range(n):
        for i in range(n-1):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]

if __name__ == "__main__":
    pass
