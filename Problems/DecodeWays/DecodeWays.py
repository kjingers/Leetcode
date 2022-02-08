'''
This "number of Ways" problem is similar to climbingStarts. We we go through s, we have 2 options:

1. Just 1 'step'. Decode s[i]. Go to index i + 1
2. If 10 <= s[i:i+2] <= 26, then we take two steps

if s[index] == 0, then we return 0, since there are no one or two digit encodings where the
first digit is 0.



'''

# Brute Force
class Solution:
    def numDecodings(self, s: str) -> int:
        
        dp = [-1 for _ in range(len(s))]
        return self.numDecodings_rec(dp, s, 0)
    
    def numDecodings_rec(self, dp, s, index):
        
        # Base Cases
        if index == len(s):
            return 1
        
        if s[index] == "0":
            return 0
        
        if dp[index] != -1:
            return dp[index]
        
        oneDigit = self.numDecodings_rec(dp, s, index + 1)
        twoDigit = 0
        if index <= len(s) - 2 and "10" <= s[index:index + 2] <= "26":
            twoDigit = self.numDecodings_rec(dp, s, index + 2)
            
        dp[index] = oneDigit + twoDigit
        return dp[index]
        
