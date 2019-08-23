import re

class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        if not s:
            return False
        pat = re.compile('\\A[\\+\\-]?(((\\d+)(\\.\\d+)?)|(\\.\\d+)|(\\d+\\.))(e[\\+\\-]?\\d+)?\\Z')
        return pat.match(s) != None
