'''
Sliding window using Counter. Tricky thing is we need to keep track of all matched characters of pattern.
'''

from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        minLength = len(s) + 1
        subStart = 0
        
        matched = 0
        
        counts = Counter(t)
        start = 0
        
        for end in range(len(s)):
            
            rightChar = s[end]
            
            if rightChar in counts:
                counts[rightChar] -= 1
                if counts[rightChar] >= 0: # Only increment matched if productive
                    matched += 1
                    
            while matched == len(t):
                if (end - start + 1) < minLength:
                    minLength = end - start + 1
                    subStart = start
                
                leftChar = s[start]
                if leftChar in counts:
                    if counts[leftChar] >= 0:
                        matched -= 1
                    counts[leftChar] += 1
                start += 1
                
        return "" if minLength > len(s) else s[subStart:subStart + minLength]
            
        
        
        
