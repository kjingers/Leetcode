'''
Sliding Window Problem.

1. Put the counts of each letter in t into a dict.
2. Increase size of window until window contains all letters of t
3. Shrink window while window has all letters of t
4. Update minLen, minStart, minEnd
'''

from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if len(t) > len(s):
            return ""
        
        d = Counter(t)
        start = 0
        
        outStr = ""
        
        for end in range(len(s)):
            endChar = s[end]
            
            if endChar in d:
                d[endChar] -= 1
            
            while all(val <= 0 for val in d.values()):

                if len(outStr) == 0 or (end - start + 1) < len(outStr):
                    outStr = s[start:end + 1]
                
                startChar = s[start]
                if startChar in d:
                    d[startChar] += 1
                
                start += 1
            
        return outStr
                
        
            
        
        
