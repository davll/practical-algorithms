OPERATORS = ['+', '-', '*', '/']

PRECEDENCE = {
    '+': 2,
    '-': 2,
    '*': 3,
    '/': 3,
}

def infix_to_rpn(tokens):
    result = []
    opstack = []
    for tok in tokens:
        if tok in OPERATORS:
            while opstack and opstack[-1] != '(' and PRECEDENCE[opstack[-1]] >= PRECEDENCE[tok]:
                x = opstack.pop()
                result.append(x)
            opstack.append(tok)
        elif tok == '(':
            opstack.append(tok)
        elif tok == ')':
            while opstack[-1] != '(':
                result.append(opstack.pop())
            assert opstack[-1] == '('
            opstack.pop()
        else:
            result.append(tok)
    while opstack:
        result.append(opstack.pop())
    return result

RPN_OPERATORS = {
    '+': (2, lambda x, y: x + y),
    '-': (2, lambda x, y: x - y),
    '*': (2, lambda x, y: x * y),
    '/': (2, lambda x, y: x // y)
}

def eval_rpn(tokens):
    stack = []
    for token in tokens:
        if token in RPN_OPERATORS:
            n, f = RPN_OPERATORS[token]
            args = [stack.pop() for _ in range(n)]
            args.reverse()
            result = f(*args)
            stack.append(result)
        else:
            stack.append(int(token))
    assert len(stack) == 1
    return stack[-1]

def tokenize(s):
    i, n = 0, len(s)
    while i < n:
        if s[i].isspace():
            i += 1
        elif s[i] in ['+', '-', '*', '/', '(', ')']:
            yield s[i]
            i += 1
        else:
            j = i + 1
            while j < n and s[j].isdigit():
                j += 1
            yield int(s[i:j])
            i = j

class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        return eval_rpn(infix_to_rpn(tokenize(s)))
