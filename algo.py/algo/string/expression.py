# Expression Parsing

from collections import namedtuple

Op = namedtuple('Op', ['name', 'symbol', 'precedence'])

OPERATORS = {
    '+': Op('add', '+', 0),
    '-': Op('sub', '-', 0),
    '*': Op('mul', '*', 0),
    '/': Op('div', '/', 0),
}

# Shunting-yard Algorithm
#
# http://www.oxfordmathcenter.com/drupal7/node/628
# https://en.wikipedia.org/wiki/Shunting-yard_algorithm
def infix_to_postfix(tokens):
    pass

def eval_postfix(tokens):
    pass
