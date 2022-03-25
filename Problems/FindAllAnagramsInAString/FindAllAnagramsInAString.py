'''
Classic Sliding Window. Use "matched" so we can keep track of how many distint characters we have matched. If we have matched all distint characters, then we have a solution. Only track characters in pattern string. This is better than checking all characters every time.
'''

from collections import Counter

# Using Matched to save TIme
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        counts = Counter(p)
        
        output = []
        left = 0
        matched = 0
        
        for right in range(len(s)):
            c = s[right]
            
            if c in counts:
                counts[c] -= 1
                if counts[c] == 0:
                    matched += 1
                
            if matched == len(counts):
                output.append(left)
            
            if right >= len(p) - 1:
                leftChar = s[left]
                if leftChar in counts:
                    if counts[leftChar] == 0:
                        matched -= 1
                    counts[leftChar] += 1
                left += 1
        return output

            
        
