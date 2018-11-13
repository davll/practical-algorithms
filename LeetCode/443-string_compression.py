class Solution:
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        n = len(chars)
        k = 0
        cnt = 1
        for i in range(1, n):
            if chars[i-1] == chars[i]:
                cnt += 1
            else:
                chars[k] = chars[i-1]
                k += 1
                if cnt > 1:
                    for d in str(cnt):
                        chars[k] = d
                        k += 1
                cnt = 1
        if n > 0 and cnt > 0:
            chars[k] = chars[n-1]
            k += 1
            if cnt > 1:
                for d in str(cnt):
                    chars[k] = d
                    k += 1
        return k
