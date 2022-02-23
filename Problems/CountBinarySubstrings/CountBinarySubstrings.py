'''
Count the number of consecutive 1s or 0s as we iterate through. When counted two groups and switching to a 3rd, first:
    - Add min(# group1, # group 2) to output. This is the number of substrings between the two previous groups.
    - Make current group size the previous
'''

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        
        if len(s) == 1:
            return 0
        
        prevCount = 0
        count = 1
        ans = 0
        
        for i in range(1, len(s)):
            
            if s[i] == s[i - 1]:
                count += 1
            else:
                ans += min(prevCount, count)
                prevCount = count
                count = 1
                
        ans += min(prevCount, count)
        return ans
            
