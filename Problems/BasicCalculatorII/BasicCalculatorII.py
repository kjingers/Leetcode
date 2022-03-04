'''
Expression / possibly bracket problem, So stack can help.

Goal is to have all elements in the stack such that we can sum them up to get the answer

Note: 
'''

from collections import deque

class Solution:
    
    def calculate(self, s: str) -> int:
        i = 0
        num = 0
        stack = deque()
        sign = "+"
        
        while i < len(s):
            
            if s[i].isdigit():
                num = num * 10 + int(s[i])
                
            if s[i] in "+-*/" or i == len(s) - 1:
                self.update(sign, num, stack)
                num = 0
                sign = s[i]
            i += 1
        
        return sum(stack)
        
        
      
    # Updates stack in place depending on previous operation
    def update(self, op, num, stack):
        if op == "+":
            stack.append(num)
        elif op == "-":
            stack.append(-num)
        elif op == "*":
            stack.append(stack.pop() * num)
        elif op == "/":
            stack.append(int(stack.pop() / num))
            
    
        
    
        
