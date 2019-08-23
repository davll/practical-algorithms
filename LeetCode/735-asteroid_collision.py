class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        s = []
        for x in asteroids:
            if x > 0:
                s.append(x)
            elif x < 0:
                while s and s[-1] > 0:
                    if s[-1] < -x:
                        s.pop()
                    elif s[-1] > -x:
                        x = 0
                        break
                    else:
                        s.pop()
                        x = 0
                        break
                if x != 0:
                    s.append(x)
        return s
