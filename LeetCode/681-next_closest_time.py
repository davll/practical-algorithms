# https://leetcode.com/problems/next-closest-time/

class Solution:
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        h, m = time.split(':')
        digits = list(set(map(int, h+m)))
        digits.sort()
        n = len(digits)
        h = list(map(lambda c: digits.index(int(c)), h))
        m = list(map(lambda c: digits.index(int(c)), m))
        #print("digits = {d}".format(d=digits))
        #print("h = {h}".format(h=h))
        #print("m = {m}".format(m=m))
        m[1] += 1
        if m[1] >= n:
            m[0], m[1] = m[0]+1, 0
        if m[0] >= n or digits[m[0]] >= 6:
            m[0] = 0
            h[1] = h[1]+1
        if h[1] >= n:
            h[0], h[1] = h[0]+1, 0
        if h[0] >= n or digits[h[0]] > 2 or (digits[h[0]] == 2 and digits[h[1]] > 3):
            h[0], h[1] = 0, 0
        return ''.join(map(lambda x: str(digits[x]), h)) + ':' + ''.join(map(lambda x: str(digits[x]), m))

#if __name__ == "__main__":
#    s = Solution().nextClosestTime("23:59")
#    print(s)
