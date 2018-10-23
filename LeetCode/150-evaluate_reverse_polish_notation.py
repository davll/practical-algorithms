from math import trunc

OPERATORS = {
    '+': (2, lambda x, y: x + y),
    '-': (2, lambda x, y: x - y),
    '*': (2, lambda x, y: x * y),
    '/': (2, lambda x, y: int(trunc(x / y)))
}

def eval_rpn(tokens):
    stack = []
    for token in tokens:
        if token in OPERATORS:
            n, f = OPERATORS[token]
            args = [stack.pop() for _ in range(n)]
            args.reverse()
            result = f(*args)
            #print("{r} = {op} {args}".format(op=token, args=args, r=result))
            stack.append(result)
        else:
            stack.append(int(token))
    assert len(stack) == 1
    return stack[-1]

class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        return eval_rpn(tokens)

if __name__ == "__main__":
    tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    ans = Solution().evalRPN(tokens)
    print(str(ans))
