'''
Standard sliding window problem
    - Increase window until repeating character (window size > len(dict))
    - Shrink window until no repeating characters (above condition false)
    - Update global max
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if not s:
            return 0
        
        maxLen = 0
        currChars = {}
        
        start = 0
        for end in range(len(s)):
            
            if s[end] not in currChars:
                currChars[s[end]] = 0
                
            currChars[s[end]] += 1
            
            while (end - start + 1) > len(currChars):
                currChars[s[start]] -= 1
                
                if currChars[s[start]] == 0:
                    del currChars[s[start]]
                    
                start += 1
                
            maxLen = max(maxLen, end - start + 1)
            
        return maxLen
            
        
