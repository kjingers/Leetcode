'''
We can use stack . As we iterate through:
    - If '(', add index to stack
    - If ')', 
        - if stack empty, then remove from list
        - If not empty, pop from stack
'''

from collections import deque

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        s = list(s)
        stack = deque()
        
        
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')':
                if stack:
                    stack.pop()
                else:
                    s[i] = ''
        
        # Everything left on stack much be removed
        while stack:
            s[stack.pop()] = ''
        
        return ''.join(s)
        
        
        
        
