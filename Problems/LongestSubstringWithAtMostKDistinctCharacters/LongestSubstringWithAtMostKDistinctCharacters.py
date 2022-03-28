'''
Grow window until > k distinct characters. Then shrink to satisfy
'''

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        maxSubarray = 0
        start = 0
        d = {}
        
        for end, char in enumerate(s):
            d[char] = d.get(char, 0) + 1
            
            while len(d) > k:
                leftChar = s[start]
                
                d[leftChar] -= 1
                if d[leftChar] == 0:
                    del d[leftChar]
                    
                start += 1
            
            maxSubarray = max(maxSubarray, end - start + 1)
        
        return maxSubarray
            
            
        
        
