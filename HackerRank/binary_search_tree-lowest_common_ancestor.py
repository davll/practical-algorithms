# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
'''

def lca(root, v1, v2):
    if v1 > v2:
        v1, v2 = v2, v1
    t = root
    while True:
        if v2 < t.info:
            t = t.left
        elif t.info < v1:
            t = t.right
        elif v1 < t.info and t.info < v2:
            return t
        else:
            return t
