'''

We can iterate through the string. At each index, check all words in wordDict to see if any end at current index.
If a word ends at current index, we mark dp[i] = True, if dp[i - len(word)] == True. This means that
a word ends at the current index, and also a previous word ended at the index before this word.

Time Complexity: O(nk) where n is length of s and k is number of words in wordDict



'''

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        dp = [False for _ in range(len(s) + 1)]
        
        dp[0] = True
        
        for i in range(len(s) + 1):
            for w in wordDict:
                if s[i - len(w):i] == w and dp[i - len(w)]:
                    dp[i] = True
                    
        return dp[-1]
                    
            
        
