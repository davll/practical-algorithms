# Expression Parsing

OPERATORS = ['+', '-', '*', '/']

PRECEDENCE = {
    '+': 2,
    '-': 2,
    '*': 3,
    '/': 3,
}

# Shunting-yard Algorithm
#
# http://www.oxfordmathcenter.com/drupal7/node/628
# https://en.wikipedia.org/wiki/Shunting-yard_algorithm
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
    '/': (2, lambda x, y: x / y)
}

# Evaluate Reverse Polish Notation
def eval_postfix(tokens):
    stack = []
    for token in tokens:
        if token in RPN_OPERATORS:
            n, f = RPN_OPERATORS[token]
            args = [stack.pop() for _ in range(n)]
            args.reverse()
            result = f(*args)
            #print("{r} = {op} {args}".format(op=token, args=args, r=result))
            stack.append(result)
        else:
            stack.append(int(token))
    assert len(stack) == 1
    return stack[-1]
