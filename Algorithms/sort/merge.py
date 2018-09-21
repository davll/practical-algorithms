def merge(a, b):
    m, n = len(a), len(b)
    c = [0] * (m+n)
    i, j, k = 0, 0, 0
    while i < m and j < n:
        if a[i] <= b[j]:
            c[k] = a[i]
            i += 1
        elif a[i] > b[j]:
            c[k] = b[j]
            j += 1
        k += 1
    if i < m:
        c[k:] = a[i:]
    if j < n:
        c[k:] = b[j:]
    return c

if __name__ == "__main__":
    pass
