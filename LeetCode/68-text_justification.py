# https://leetcode.com/problems/text-justification/

class Solution:
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        lines = []
        occupied = maxWidth
        for word in words:
            sz = len(word)
            if occupied + 1 + sz > maxWidth:
                # create new line
                occupied = sz
                lines.append([word])
            else:
                # append to last line
                occupied += 1 + sz
                lines[-1].append(word)
        #print(str(lines))
        if not lines:
            return []
        result = []
        for line in lines[:-1]:
            assert line
            total_spaces = maxWidth - sum(map(len, line))
            if len(line) > 1:
                min_spaces = total_spaces // (len(line)-1)
                remainders = total_spaces % (len(line)-1)
                #print("TOTAL = {t}, MIN = {m}, R = {r}".format(t=total_spaces, m=min_spaces, r=remainders))
                text = line[:1]
                for i in range(1, len(line)):
                    text.append(' ' * (min_spaces + int(remainders >= i)))
                    text.append(line[i])
                result.append(''.join(text))
            else:
                result.append(line[0] + ' ' * total_spaces)
        result.append(' '.join(lines[-1]) + ' ' * (maxWidth - sum(map(len, lines[-1])) - (len(lines[-1])-1)))
        return result
