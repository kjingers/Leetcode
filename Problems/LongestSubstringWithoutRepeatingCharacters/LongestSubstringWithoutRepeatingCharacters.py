'''
Standard sliding window problem
    - Increase window until repeating character (window size > len(dict))
    - Shrink window until no repeating characters (above condition false)
    - Update global max
    
O(n) time
O(k) --> O(1) Space. K is number of distint characters. So worst case O(26) -> O(1)
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if not s:
            return 0
        
        maxLen = 0
        d = {}
        
        start = 0
        for end in range(len(s)):
            
            # We've seen this character before. If it was before our current window,
            # then the start will be the same (no need to adjust). Else, we need
            # to move start to last seen index + 1, so that s[end] is the only occurence of the letter
            # in our window
            
            if s[end] in d:
                start = max(start, d[s[end]] + 1)
                
            maxLen = max(maxLen, end - start + 1)
            
            d[s[end]] = end
            
            
        return maxLen
            
        
