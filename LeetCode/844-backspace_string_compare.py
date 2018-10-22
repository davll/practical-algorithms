class Solution:
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        # i: current index
        # si: how many characters to skip
        def digest_backspaces(A, i, si):
            while i >= 0:
                # increase skip counter if backspace
                if A[i] == '#':
                    i, si = i-1, si+1
                # skip characters except backspaces
                elif si > 0:
                    i, si = i-1, si-1
                # quit if no backspace left
                else:
                    break
            return (i, si)
        i, j = len(S)-1, len(T)-1
        si, sj = 0, 0
        while True:
            # process backspaces and skip characters
            i, si = digest_backspaces(S, i, si)
            j, sj = digest_backspaces(T, j, sj)
            # boundary check
            if i < 0 or j < 0:
                break
            # check matching
            assert S[i] != '#'
            assert T[j] != '#'
            assert si == 0
            assert sj == 0
            if S[i] == T[j]:
                i, j = i-1, j-1
            else:
                return False
        # process remaining backspaces
        i, si = digest_backspaces(S, i, si)
        j, sj = digest_backspaces(T, j, sj)
        return i < 0 and j < 0
