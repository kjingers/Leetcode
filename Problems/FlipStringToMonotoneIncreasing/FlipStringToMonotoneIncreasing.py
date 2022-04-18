'''
"Minimum Number" -> Greedy / DP?

For each 0, to make monotone increasing, we can either:
    1. Flip to 1. res += 1
    2. Keep as 0, but flip all prev seen 1s to 0. res = onesSeen
    
Dynamic Programming. At each index, we calculate the minimum number of flips to maintain monoone increasing

if nums[i] == "0": dp[i] = min(onesSeen, dp[i - 1] + 1)
else: dp[i] = dp[i - 1]
'''

class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        onesSeen = 0
        numFlips = 0
        count = 0
        
        for num in s:
            if num == "0":
                keepZero = onesSeen
                flip = numFlips + 1
                numFlips = min(keepZero, flip)                
            else:
                onesSeen += 1
        return numFlips
            
            
        
