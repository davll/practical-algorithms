# https://leetcode.com/problems/simplify-path/

def normalize_path(path):
    result = []
    for x in filter(bool, path.split('/')):
        if x == '.':
            pass
        elif x == '..':
            if result:
                result.pop()
        else:
            result.append(x)
    return '/' + '/'.join(result)

class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        return normalize_path(path)

#if __name__ == "__main__":
#    print(normalize_path("/a//b////c/d//././/.."))
