'''
Can do normal sort and compare in O(nlogn)
Can do counting sort since only 26 letters for O(n + 26) (I think)

Can use hash map of count
'''

from collections import Counter


# Hash Map w/ Frequency Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        d = Counter(t)
        
        for c in s:
            if c not in d:
                return False
            
            d[c] -= 1
            if d[c] == 0:
                del d[c]
                
        return True
        
        
