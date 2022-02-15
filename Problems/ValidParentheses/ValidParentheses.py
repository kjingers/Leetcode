'''
Can use a stack to push the open brackets as we see then. When we see a closed bracket, we pop
from the stack and compare to see if it's the same type.

We can initialize a hashmap where key=open brackets and value=closed, so that we can easily lookup
to see if both brackets are the same type.
'''

from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        
        d = {'(': ')', '[': ']', '{': '}'}
        stack = deque()
        
        for c in s:
            
            # If open bracket
            if c in d:
                stack.append(c)
            else: # Closed Bracket
                if not stack or d[stack.pop()] != c:
                    return False
                
        return False if stack else True
        
        
