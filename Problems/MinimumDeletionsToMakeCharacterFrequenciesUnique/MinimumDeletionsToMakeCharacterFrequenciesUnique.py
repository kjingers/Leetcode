'''
Can create dictionary of counts of each letter. 
    - Then, we loop through the frequencies and add them to a set. 
    - If we get a frequency that already exists in the set, we keep subtracting until it is unique
'''
from collections import Counter

class Solution:
    def minDeletions(self, s: str) -> int:
        counts = Counter(s)
        seen = set()
        deletions = 0
        
        for count in counts.values():
            
            while count > 0 and count in seen:
                count -= 1
                deletions += 1
            
            seen.add(count)
            
        return deletions
        
        
        
