'''
Intuition: Parenthesis so likely stack. Need most inner k + string most accessible (on top) and process older stuff (outer) later.

As we iterate through the string, we have to handle 4 cases
    - If digit, add k = k * 10 + int(c)
    - If letter, add it to current string
    - If open bracket, Push currentString and k onto stack. Reset current string and k.
    - If closed bracket, need to pop prev_k and prev_str. currentString = prev_str + k * currentString
    
    
We know we need to handle 4 cases. Also, if we get a "]", we know we need to decode part of a string

'''

from collections import deque

class Solution:
    def decodeString(self, s: str) -> str:
        stack = deque()
        k = 0
        currentStr = ""
        
        for c in s:
            if c.isdigit():
                k = k * 10 + int(c)
            elif c == "[":
                # currentString was before k
                stack.append((currentStr, k))
                currentStr = ""
                k = 0
            elif c == "]":
                prevStr, prevK = stack.pop()
                currentStr = prevStr + prevK * currentStr
            else:
                currentStr += c
        
        return currentStr
        
