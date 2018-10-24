def tokenize(s):
    i, n = 0, len(s)
    while i < n:
        if s[i].isspace():
            i += 1
        elif s[i] in ['+', '-', '*', '/']:
            yield s[i]
            i += 1
        else:
            j = i + 1
            while j < n and s[j].isdigit():
                j += 1
            yield int(s[i:j])
            i = j

OPERATORS = ['+', '-', '*', '/']

PRECEDENCE = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2
}

def eval_tokens(tokens):
    result = []
    opstack = []
    def pop_op():
        a2 = result.pop()
        a1 = result.pop()
        op = opstack.pop()
        if op == '+':
            result.append(a1 + a2)
        elif op == '-':
            result.append(a1 - a2)
        elif op == '*':
            result.append(a1 * a2)
        elif op == '/':
            result.append(a1 // a2)
        else:
            raise RuntimeError()
    for tok in tokens:
        if tok in OPERATORS:
            while opstack and PRECEDENCE[opstack[-1]] >= PRECEDENCE[tok]:
                pop_op()
            opstack.append(tok)
        else:
            result.append(tok)
    while opstack:
        pop_op()
    return result[-1]

class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        return eval_tokens(tokenize(s))
