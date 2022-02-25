'''
Pretty straightforward.

    - If we see a '(', then add one to (needRight)
    - If we see a ')', decrement needRight. If needRight is 0, increament needLeft
    - Return needRight + needLeft
'''

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        
        needLeft, needRight = 0, 0
        
        for c in s:
            if c == '(':
                needRight += 1
            else:
                if needRight > 0:
                    needRight -= 1
                else:
                    needLeft += 1
                    
        return needLeft + needRight
        
