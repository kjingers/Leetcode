'''
OOP Design Question.

Basically, we want to return the root node of expression tree. We want all nodes to have evaluate method implemented from abstract Node class. So that calling evaluate on operator node calls evaluate on child nodes to solve the expression.
'''

import abc 
from abc import ABC, abstractmethod 
"""
This is the interface for the expression tree Node.
You should not remove it, and you can define some classes to implement it.
"""

class Node(ABC):
    @abstractmethod
    # define your fields here
    def evaluate(self) -> int:
        pass
        
        
class NumericNode(Node):
    def __init__(self, value):
        self.value = value
        
    def evaluate(self):
        return self.value
    
class OperatorNode(Node):
    def __init__(self, left, right):
        self.left = left
        self.right = right
        
    #def evaluate(self):
        #pass
    
class Plus(OperatorNode):
    def evaluate(self):
        return self.left.evaluate() + self.right.evaluate()
    
class Minus(OperatorNode): 
    def evaluate(self):
        return self.left.evaluate() - self.right.evaluate()
    
class Mult(OperatorNode):
    def evaluate(self):
        return self.left.evaluate() * self.right.evaluate()
    
class Div(OperatorNode):
    def evaluate(self):
        return self.left.evaluate() // self.right.evaluate()
    
    
    """    
This is the TreeBuilder class.
You can treat it as the driver code that takes the postinfix input
and returns the expression tree represnting it as a Node.
"""

class TreeBuilder(object):
    def buildTree(self, postfix: List[str]) -> 'Node':
        stack = deque()
        
        # Maps Operator to Class
        operators = {'+': Plus, '-': Minus, '*': Mult, '/': Div}
        for token in postfix:
            if token in operators:
                R = stack.pop()
                L = stack.pop()
                stack.append(operators[token](L, R))
            else:
                stack.append(NumericNode(int(token)))
            #print(stack)
        
        return stack[0]
"""
Your TreeBuilder object will be instantiated and called as such:
obj = TreeBuilder();
expTree = obj.buildTree(postfix);
ans = expTree.evaluate();
"""
        
