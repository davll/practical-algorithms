from sys import stdin, stdout, stderr

N = 10

def crosswordPuzzle(crossword, words):
    # scan horizontally
    horizontal = []
    for i in range(N):
        a = None
        for j in range(N):
            if a is None and crossword[i][j] == '-':
                a = j
            elif a is not None and crossword[i][j] != '-':
                horizontal.append((i, (a, j)))
                a = None
        if a is not None:
            horizontal.append((i, (a, N)))
    # scan vertically
    vertical = []
    for j in range(N):
        a = None
        for i in range(N):
            if a is None and crossword[i][j] == '-':
                a = i
            elif a is not None and crossword[i][j] != '-':
                vertical.append(((a, i), j))
                a = None
        if a is not None:
            vertical.append(((a, N), j))
    used_horiz = [False] * len(horizontal)
    used_verti = [False] * len(vertical)
    stderr.write("horiz = " + str(horizontal) + '\n')
    stderr.write("verti = " + str(vertical) + '\n')
    # do backtracking
    def print_sol():
        for i in range(N):
            stdout.write(''.join(crossword[i]) + '\n')
    #
    def backtrack_horiz(word_i):
        w = words[word_i]
        for h in range(len(horizontal)):
            if used_horiz[h]:
                continue
            i, (j0, j1) = horizontal[h]
            if (j1-j0) != len(w):
                continue
            # check word match
            ok = True
            for j in range(j0, j1):
                c = crossword[i][j]
                if c != '-' and c != w[j-j0]:
                    ok = False
                    break
            if not ok:
                continue
            # fill and go down
            used_horiz[h] = True
            temp = crossword[i][j0:j1]
            for j in range(j0, j1):
                crossword[i][j] = w[j-j0]
            backtrack(word_i + 1)
            for j in range(j0, j1):
                crossword[i][j] = temp[j-j0]
            used_horiz[h] = False
    #
    def backtrack_verti(word_i):
        w = words[word_i]
        for v in range(len(vertical)):
            if used_verti[v]:
                continue
            (i0, i1), j = vertical[v]
            if (i1-i0) != len(w):
                continue
            # check word match
            ok = True
            for i in range(i0, i1):
                c = crossword[i][j]
                if c != '-' and c != w[i-i0]:
                    ok = False
                    break
            if not ok:
                continue
            # fill and go down
            used_verti[v] = True
            temp = [crossword[i][j] for i in range(i0, i1)]
            for i in range(i0, i1):
                crossword[i][j] = w[i-i0]
            backtrack(word_i + 1)
            for i in range(i0, i1):
                crossword[i][j] = temp[i-i0]
            used_verti[v] = False
    #
    def backtrack(word_i):
        if word_i == len(words):
            print_sol()
        else:
            backtrack_horiz(word_i)
            backtrack_verti(word_i)
    backtrack(0)

if __name__ == "__main__":
    crossword = [
        list(stdin.readline().rstrip())
        for _ in range(N)
    ]
    words = list(map(list, stdin.readline().rstrip().split(';')))
    crosswordPuzzle(crossword, words)
